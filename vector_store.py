import faiss
import numpy as np
import pickle
import os
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self, model_name='all-MiniLM-L6-v2', save_path='faiss_index.pkl'):
        """
        初始化 VectorStore，加载 embedding 模型并初始化 FAISS 索引。
        """
        print(f"正在加载 Embedding 模型: {model_name}...")
        self.model = SentenceTransformer(model_name)
        print("Embedding 模型加载完成。")
        self.save_path = save_path
        self.documents = []
        self.index = None
        
        # 尝试加载现有索引
        if os.path.exists(self.save_path):
            print(f"正在从 {self.save_path} 加载现有索引...")
            self.load()
            print(f"索引加载完成，共 {len(self.documents)} 条文档。")
        else:
            # 维度取决于模型 (all-MiniLM-L6-v2 是 384)
            self.dimension = 384
            self.index = faiss.IndexFlatL2(self.dimension)

    def add_documents(self, documents: list[str]):
        """
        将文本列表转换为向量并存入数据库。
        """
        if not documents:
            return
            
        # 生成 Embeddings
        embeddings = self.model.encode(documents)
        embeddings = np.array(embeddings).astype('float32')
        
        # 存入 FAISS 索引
        self.index.add(embeddings)
        
        # 保存原始文档
        self.documents.extend(documents)
        
        # 持久化存储
        self.save()

    def search(self, query: str, top_k=3):
        """
        根据查询语句，返回数据库中最相似的 top_k 段文本。
        """
        if not self.documents:
            return []
            
        # 查询向量化
        query_embedding = self.model.encode([query])
        query_embedding = np.array(query_embedding).astype('float32')
        
        # FAISS 检索
        distances, indices = self.index.search(query_embedding, top_k)
        
        # 返回匹配的文档内容
        results = []
        for i in indices[0]:
            if i != -1 and i < len(self.documents):
                results.append(self.documents[i])
        return results

    def save(self):
        """
        将索引和文档保存到本地文件。
        """
        # FAISS 索引不能直接 pickle，需要先写入一个字节数组
        # 但对于 IndexFlatL2 这种小型索引，我们可以通过这种简化的方式序列化相关数据
        with open(self.save_path, 'wb') as f:
            pickle.dump({
                'documents': self.documents,
                'index_data': faiss.serialize_index(self.index)
            }, f)

    def load(self):
        """
        从本地加载索引和文档。
        """
        with open(self.save_path, 'rb') as f:
            data = pickle.load(f)
            self.documents = data['documents']
            self.index = faiss.deserialize_index(data['index_data'])
