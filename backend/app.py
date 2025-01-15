from flask import Flask, request, render_template, jsonify
import pandas as pd
from sentence_transformers import SentenceTransformer, util

app = Flask(__name__, template_folder="../backend/templates", static_folder="../static")

# Charger les données
data = pd.read_csv('../data/diabetes_data.csv')
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Fonction de recherche NLP avancée
def get_advanced_answer(user_question):
    embeddings = model.encode(data['questions'].tolist(), convert_to_tensor=True)
    query_embedding = model.encode(user_question, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(query_embedding, embeddings)[0]
    best_match_idx = cosine_scores.argmax().item()
    return data.iloc[best_match_idx]['answers']

# Page d'accueil
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint de question avec retour JSON
@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.form['question']
    answer = get_advanced_answer(user_question)
    return jsonify({"answer": answer})

# Lancer le serveur Flask
if __name__ == "__main__":
    app.run(debug=True)
