import faiss
from sentence_transformers import SentenceTransformer

def create_embeddings(texts):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(texts, convert_to_tensor=False)  # Use convert_to_tensor=False for FAISS compatibility
    return embeddings

def store_embeddings(embeddings, index_path='vector_database.index'):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    faiss.write_index(index, index_path)
    print("Vector database created and saved.")
