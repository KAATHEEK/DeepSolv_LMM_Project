from flask import Flask, request, jsonify, render_template
import faiss
from sentence_transformers import SentenceTransformer

# Initialize Flask app
app = Flask(__name__)

# Load the FAISS index and the SentenceTransformer model
index = faiss.read_index('vector_database.index')
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query_faiss():
    query = request.form['query']
    query_embedding = model.encode([query])
    D, I = index.search(query_embedding, k=5)  # k is the number of nearest neighbors to retrieve
    results = [int(i) for i in I[0]]  # Convert results to a list of integers
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
