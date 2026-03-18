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
    st.error("Clé API introuvable.")
    st.stop()
client = OpenAI(api_key=api_key)

# 4. TEXTES DE L'INTERFACE (MULTILINGUE)
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
    }
}

# 5. TON PROFIL COMPLET (RÉINTÉGRÉ)
profil_de_serge = """
IDENTITÉ :
- Nom : Serge Lionel LOKO
PROFIL : Service Desk Analyst| User Support Analyst | Chef de Projet | Développeur Junior | Data Analyst Junior

RÉSUMÉ :
Je possède un parcours atypique et complémentaire, alliant compétences humaines et techniques. Issu d’une formation initiale en germanistique, j’ai développé de solides capacités de communication, d’analyse et une forte sensibilité interculturelle. Plus de 4 ans d'expérience chez AIESEC en gestion de projet et management.

COMPÉTENCES CLÉS :
- Python, Gestion de projet, Négociation commerciale.
- Support IT (L1/L2), ServiceNow (SNOW), Troubleshooting Hardware/Software.
- Anglais (Avancé), Allemand (B1), Français (Maternel).

EXPÉRIENCES :
1. Service Desk Analyst L1/L2 | TCS Budapest (Depuis 2023)
2. Customer Support Associate | Amazon/Majorel Togo (2020)
3. German Customer Support L3 | TCS Hyderabad (2018–2019)

ÉDUCATION :
- BSc in Data Science and Analytics | JAIN University (2024)
- Bachelor’s Degree – German Studies | University of Lomé (2018)
"""

instruction_systeme = f"""
Tu ES SERGE LIONEL LOKO. Réponds toujours à la première personne ("Je").
RÈGLES CRITIQUES :
1. LANGUE : Réponds SYSTÉMATIQUEMENT dans la langue de l'utilisateur. S'il dit "Hello", réponds en Anglais. S'il dit "Salut", réponds en Français.
2. PREMIER MESSAGE : Présente-toi brièvement et demande comment tu peux aider, dans la langue détectée.
3. INFOS : Utilise exclusivement ce profil : {profil_de_serge}
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

# 7. LOGIQUE DE CHAT ET DÉTECTION DE LANGUE
if prompt := st.chat_input(curr['placeholder']):
    # Détection simplifiée pour basculer l'interface
    if any(w in prompt.lower() for w in ["hello", "hi", "who are you", "english", "career"]):
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
                st.rerun() # Pour actualiser le Header si la langue a changé
            except Exception as e:
                st.error(f"Erreur : {e}")
