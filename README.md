# Chatbot Diabète

Ce projet est un chatbot interactif conçu pour répondre à des questions sur le diabète en utilisant l'intelligence artificielle. Il est construit avec Flask (backend), SentenceTransformer pour le NLP, et une interface web HTML/CSS/JS pour l'interaction utilisateur.

## 📂 Structure du projet

```plaintext
backend/
├── app.py                   # Serveur Flask
├── templates/
│   └── index.html           # Interface Web
├── static/
│   ├── style.css            # Design
│   └── script.js            # Logique client
├── data/
│   └── diabetes_data.csv    # Données utilisées par le modèle
scraping/
├── scraper.py               # Script de scraping pour extraire les données
README.md                    # Documentation du projet
requirements.txt             # Dépendances Python
```

---

## 🚀 Démarrage rapide

### **1. Cloner le projet**
```bash
git clone <repo-url>
cd diabetes_chatbot
```

### **2. Créer l'environnement virtuel (recommandé)**
```bash
python -m venv venv
source venv/bin/activate  # Sur Mac/Linux
venv\Scripts\activate    # Sur Windows
```

### **3. Installer les dépendances**
```bash
pip install -r requirements.txt
```

### **4. Lancer le serveur Flask**
```bash
python backend/app.py
```

### **5. Accéder à l'application Web**
Ouvrez votre navigateur et accédez à :
```plaintext
http://127.0.0.1:5000
```

---

## 📊 **Données Utilisées**
Le projet utilise un fichier `diabetes_data.csv` contenant :
- **Questions** : Questions courantes sur le diabète.
- **Réponses** : Réponses associées fournies par des sources fiables.

---

## 🧠 **Fonctionnalités**
- **Traitement du langage naturel (NLP)** avec `SentenceTransformer`.
- **Interface Web interactive** avec HTML, CSS et JavaScript.
- **Design responsive et moderne.**
- **Scraping de données intégré** pour extraire des informations sur le diabète.

---

## 🧪 **Technologies Utilisées**
- **Backend :** Flask
- **NLP :** SentenceTransformer (MiniLM)
- **Frontend :** HTML, CSS, JavaScript
- **Base de données :** CSV (diabetes_data.csv)

---

## 📦 **Améliorations futures**
- [ ] Ajout de la synthèse vocale (TTS).
- [ ] Amélioration du scraping avec Selenium.
- [ ] Déploiement sur un serveur cloud (Heroku/AWS).

---

## 📃 **Licence**
Utilisation et modifications libres avec mention de l'auteur.

---

## 🙌 **Contributions**
Les contributions sont les bienvenues !

1. Forkez le projet.
2. Créez une branche : `git checkout -b feature/ma-fonctionnalite`
3. Committez vos modifications : `git commit -m 'Ajout d'une nouvelle fonctionnalité'`
4. Poussez votre branche : `git push origin feature/ma-fonctionnalite`
5. Créez une Pull Request.

---

🎯 **Auteur :** Papa Seydou Wane
🎯 **E-mail :** Papa Seydou WANE

