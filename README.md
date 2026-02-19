🤖 Sorbonne AI Multi-Hub : Unified Chat Interface
Ce projet est une plateforme de discussion universelle développée à Sorbonne Université. Elle permet de basculer instantanément entre les meilleurs modèles du marché (OpenAI, Google Gemini, Groq) au sein d'une interface unique et fluide.

🌟 Points Forts
Multi-Fournisseur (Agnostique) : Support natif pour GPT-4o, Gemini 1.5 Pro et Llama 3.3 via une interface de sélection dynamique.

Comparaison en Temps Réel : Idéal pour tester la pertinence des réponses entre différents modèles sur une même question.

Architecture "Stateful" : Gestion de la mémoire via st.session_state qui persiste même lors du changement de modèle en cours de conversation.

Zéro Latence (Groq) : Intégration optimisée pour les modèles Llama ultra-rapides.

🛠️ Stack Technique
Frontend : Streamlit (Composants Chat avancés).

Orchestration : LangChain (méthodes invoke unifiées pour tous les fournisseurs).

Modèles supportés :

OpenAI : gpt-4o, gpt-3.5-turbo

Google : gemini-1.5-flash, gemini-1.5-pro

Groq : llama-3.3-70b-versatile, llama-3.1-8b-instant

⚙️ Installation Rapide
Clonage & Dépendances :

Bash
git clone https://github.com/votre-username/sorbonne-ai-hub.git
pip install streamlit langchain-groq langchain-openai langchain-google-genai python-dotenv
Configuration des Clés API :
Créez un fichier .env à la racine :

Extrait de code
OPENAI_API_KEY=votre_cle
GOOGLE_API_KEY=votre_cle
GROQ_API_KEY=votre_cle
Lancement :

Bash
streamlit run app.py
🧠 Fonctionnement Interne
Le code utilise une logique de branchement conditionnel :

L'utilisateur choisit un Provider via un menu déroulant.

Le script instancie dynamiquement l'objet llm correspondant grâce à la modularité de LangChain.

L'historique des messages est formaté et envoyé au modèle sélectionné, garantissant une continuité dans le dialogue peu importe l'IA choisie.
