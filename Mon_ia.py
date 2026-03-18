import streamlit as st
from openai import OpenAI
import os

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="Serge Lionel LOKO",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. CSS ULTRA-AGRESSIF (Design Image 3)
st.markdown("""
    <style>
html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .main {
    background-color: white !important;
    color: #1E1E1E !important;
}
header, footer, #MainMenu, .stDeployButton, [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] {
    visibility: hidden !important;
    display: none !important;
}
.header-box {
    border: 2px solid #0E2A47 !important;
    padding: 40px 30px !important;
    border-radius: 12px !important;
    background-color: #FFFFFF !important;
    text-align: center !important;
    margin-top: -30px;
    margin-bottom: 35px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
}
.header-box h1 { 
    color: #0E2A47 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 30px !important;
    font-weight: 700 !important;
}
.header-box h3 { 
    color: #4A4A4A !important;
    font-size: 16px !important;
    font-weight: 400 !important;
}
[data-testid="stChatInput"] {
    border: 1px solid #0E2A47 !important;
    border-radius: 10px !important;
}
[data-testid="stChatInput"] textarea {
    border: none !important;
    box-shadow: none !important;
}
[data-testid="stChatInput"]:focus-within {
    border-color: #0E2A47 !important;
    box-shadow: 0 0 0 1px #0E2A47 !important;
}
[data-testid="stChatInputSubmitButton"] svg {
    fill: #0E2A47 !important;
}
[data-testid="stChatMessage"] p {
    color: #1E1E1E !important;
}
</style>
""", unsafe_allow_html=True)

# 3. CONNEXION OPENAI
api_key = os.environ.get("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")
if not api_key:
    st.error("Oups ! La clé API est introuvable. Vérifiez vos variables d'environnement.")
    st.stop()
client = OpenAI(api_key=api_key)

# 4. ÉTAT DE LA LANGUE ET TEXTES INTERFACE
if "lang" not in st.session_state:
    st.session_state.lang = "fr"

texts = {
    "fr": {
        "title": "Bonjour, je suis Serge Lionel LOKO",
        "subtitle": "N'hésitez pas à me poser des questions sur mon parcours et mes compétences.",
        "placeholder": "Tapez votre question..."
    },
    "en": {
        "title": "Hello, I am Serge Lionel LOKO",
        "subtitle": "Feel free to ask me anything about my career and skills.",
        "placeholder": "Type your question..."
    },
    "de": {
        "title": "Hallo, ich bin Serge Lionel LOKO",
        "subtitle": "Sie können mich gerne alles über meine Karriere und meine Fähigkeiten fragen.",
        "placeholder": "Geben Sie Ihre Frage ein..."
        }
}

# 5. PROFIL COMPLET (RÉTABLI DANS SON INTÉGRALITÉ)
profil_de_serge = """
IDENTITÉ :
- Nom : Serge Lionel LOKO
PROFIL : Service Desk Analyst| User Support Analyst | Chef de Projet | Développeur Junior | Data Analyst Junior

RÉSUMÉ :
Je possède un parcours atypique et complémentaire, alliant compétences humaines et techniques. Issu d’une formation initiale en germanistique, j’ai développé de solides capacités de communication, d’analyse et une forte sensibilité interculturelle. 
En parallèle, j’ai acquis plus de quatre années d’expérience au sein de l’une des plus grandes organisations de jeunesse au monde AIESEC, où j’ai évolué sur des missions de gestion de projets, de coordination d’équipes et de people management, avec une approche proche des enjeux RH. 
Ces expériences m’ont permis de renforcer des qualités telles que l’écoute active, l’organisation, la prise de décision, le leadership et le sens des responsabilités. 
Guidé par une passion profonde pour la technologie et la résolution de problèmes, je me suis naturellement orienté vers l’informatique. Aujourd’hui, je développe des compétences concrètes en support IT, systèmes et programmation à travers mes projets et expériences pratiques.

COMPÉTENCES CLÉS :
- Gestion de projet 
- Python (Niveau débutant mais passionné)
- Négociation commerciale
- Service Desk Support (L1 with L2 Exposure)
- Incident & Request Management (ITIL-oriented)
- Ticketing Systems (ServiceNow – SNOW)
- Hardware & Software Troubleshooting
- User Access & System Support
- IT Documentation & Knowledge Base
- Anglais (Avancé), Allemand (intermédiaire B1), Français (Langue maternelle)

EXPÉRIENCES :
1. Service Desk Analyst – L1 (with L2 Exposure) | Tata Consultancy Services (TCS) | Budapest (Since 2023)
- Support L1 & L2 troubleshooting for French-speaking users.
- Resolution of incidents (software, hardware, system access).
- Management using ServiceNow (SLA compliance).

2. Customer Support Associate – Amazon | Majorel, Togo (2020)
- Support via phone/email, conflict management.

3. German Customer Support – Level 3 | TCS | Hyderabad, India (2018–2019)
- Level 3 support tickets, SAP usage, critical tickets management.

EDUCATION:
- Autodidacte en Intelligence Artificielle (2025)
- BSc in Data Science and Analytics | JAIN University, India (2024)
- Bachelor’s Degree – German Studies | University of Lomé (2018)

TOOLS : ServiceNow (SNOW), SAP, Office 365, Teams, Jira.

SOFT SKILLS : Curieux, résilient, très bon relationnel, rigoureux, organisé, esprit d’équipe.

CONTACT :
- Email : loko.sergelionel@gmail.com
- LinkedIn : https://www.linkedin.com/in/koffi-mawugnon-serge-lionel-loko
"""

# INSTRUCTIONS SYSTÈME (AVEC RÈGLE DE LANGUE PRIORITAIRE)
instruction_systeme = f"""
Tu ES Serge Lionel LOKO. Réponds toujours à la première personne ("Je").

RÈGLE ABSOLUE : Détecte la langue de l'utilisateur et réponds EXCLUSIVEMENT dans cette langue.
- Si l'utilisateur dit "Hello", "Hi" ou écrit en anglais -> Réponds en ANGLAIS.
- Si l'utilisateur écrit en français -> Réponds en FRANÇAIS.
- Si l'utilisateur écrit en allemand -> Réponds en ALLEMAND.

Voici ton parcours et tes compétences complètes :
{profil_de_serge}

RÈGLES DE CONVERSATION :
1. Si un recruteur demande "Qui êtes-vous ?", présente-toi et demande "comment puis-je vous être utile aujourd'hui".
2. Ne t'invente pas de vie. Si une compétence n'est pas dans la liste, dis honnêtement que tu apprends vite.
3. Garde ton rôle quoi qu'il arrive.
4. Réponds toujours dans la langue dans laquelle on t'écrit
5. Sois bref, précis et professionel dans tes réponses

RÈGLE DU PREMIER CONTACT (CRITIQUE) : 
Si l'utilisateur te dit juste "Hello", "Salut", ou une salutation simple :
- NE DONNE PAS tes titres ou ton CV immédiatement.
- Réponds simplement : "Bonjour/Hello, je suis Serge Lionel LOKO. Comment puis-je vous être utile aujourd'hui ?" (dans la bonne langue).
- Attends la question suivante pour donner des détails sur ton profil.
"""

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": instruction_systeme}]

# 6. HEADER DYNAMIQUE
curr = texts[st.session_state.lang]
st.markdown(f"""
    <div class="header-box">
        <h1>{curr['title']}</h1>
        <h3>{curr['subtitle']}</h3>
    </div>
    """, unsafe_allow_html=True)

# Affichage des messages
for msg in st.session_state.messages:
    if msg["role"] != "system":
        avatar = "👤" if msg["role"] == "user" else "💼"
        with st.chat_message(msg["role"], avatar=avatar):
            st.write(msg["content"])

# 7. LOGIQUE DE CHAT ET DÉTECTION
if prompt := st.chat_input(curr['placeholder']):
    # Détection pour changer le Header (UI)
    if any(w in prompt.lower() for w in ["hello", "hi", "hey", "who are you", "english", "career"]):
        st.session_state.lang = "en"
    elif any(w in prompt.lower() for w in ["bonjour", "salut", "qui es-tu", "français", "parcours"]):
        st.session_state.lang = "fr"

    with st.chat_message("user", avatar="👤"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    contexte = [st.session_state.messages[0]] + st.session_state.messages[-6:]

    with st.chat_message("assistant", avatar="💼"):
        with st.spinner(""):
            placeholder = st.empty()
            full_response = ""
            try:
                stream = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=contexte,
                    stream=True,
                )
                for response in stream:
                    content = response.choices[0].delta.content
                    if content:
                        full_response += content
                        placeholder.markdown(full_response + "▌")
                
                placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                st.rerun() 
            except Exception as e:
                st.error(f"Erreur : {e}")
