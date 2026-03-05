import streamlit as st
from openai import OpenAI

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="Serge Lionel LOKO",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. CSS ULTRA-AGRESSIF (Supprime le rouge, les logos et force le design Image 3)
st.markdown("""
    <style>
/* --- AJOUT POUR FAIRE PARTIR LE LOGO --- */
/* Cible absolument tous les éléments de l'interface Streamlit qui affichent des logos ou des menus */
[data-testid="stHeader"], 
[data-testid="stToolbar"], 
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
#MainMenu, 
header, 
footer, 
.stAppHeader,
.st-emotion-cache-18ni7ap, 
.st-emotion-cache-zq5wmm,
.st-emotion-cache-h5rgaw {
    visibility: hidden !important;
    display: none !important;
    height: 0 !important;
}
/* --------------------------------------- */

/* Force le mode clair et neutralise les thèmes automatiques du Cloud */
html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .main {
    background-color: white !important;
    color: #1E1E1E !important;
}

/* Design du Cadre Header (Réplique Image 3) */
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

/* SUPPRESSION DU CONTOUR ROUGE SUR LA ZONE DE SAISIE */
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

/* Bouton d'envoi en Bleu Marine (SVG) */
[data-testid="stChatInputSubmitButton"] svg {
    fill: #0E2A47 !important;
}

/* Fix couleur texte messages */
[data-testid="stChatMessage"] p {
    color: #1E1E1E !important;
}
</style>
""", unsafe_allow_html=True)

# 3. CONNEXION OPENAI
try:
    api_key = st.secrets["OPENAI_API_KEY"]
except:
    st.error("Clé API manquante dans les secrets (OPENAI_API_KEY).")
    st.stop()

client = OpenAI(api_key=api_key)

# 4. TEXTES COMPLETS (PROFIL ET PARCOURS)
profil_de_serge = """
IDENTITÉ :
- Nom : Serge Lionel LOKO
PROFIL : Service Desk Analyst (L1) | L2 Exposure | User Support Analyst | Chef de Projet | Développeur Junior

RÉSUMÉ :
Je possède un parcours atypique et complémentaire, alliant compétences humaines et techniques. Issu d’une formation initiale en germanistique, j’ai développé de solides capacités de communication, d’analyse et une forte sensibilité interculturelle.

En parallèle, j’ai acquis plus de quatre années d’expérience au sein de l’une des plus grandes organisations de jeunesse au monde AIESEC, où j’ai évolué sur des missions de gestion de projets, de coordination d’équipes et de people management, avec une approche proche des enjeux RH.

Ces expériences m’ont permis de renforcer des qualités telles que l’écoute active, l’organisation, la prise de décision, le leadership et le sens des responsabilités.

Guidé par une passion profonde pour la technologie et la résolution de problèmes, je me suis naturellement orienté vers l’informatique. Aujourd’hui, je développe des compétences concrètes en support IT, systèmes et programmation à travers mes projets et expériences pratiques.

Rigoureux, organisé et orienté solutions, j’apprends rapidement et m’adapte facilement à de nouveaux environnements. J’apprécie le travail en équipe et je communique efficacement avec des profils techniques comme non techniques.

Mon objectif est d’évoluer au sein d’une entreprise où je peux apporter une réelle valeur, continuer à monter en compétences et m’inscrire sur le long terme.

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

# 5. INSTRUCTIONS SYSTÈME (LE CERVEAU)
instruction_systeme = f"""
Tu n'es pas une IA générique. TU ES SERGE LIONEL LOKO.
Tu parles toujours à la première personne du singulier ("Je", "Mon", "Mes").
Réponds de manière concise, professionnelle et directe.
Voici ton parcours et tes compétences :
{profil_de_serge}

RÈGLES DE CONVERSATION :
1. Si un recruteur te demande "Qui êtes-vous ?", présente-toi brièvement.
2. Ne t'invente pas de vie. Si une compétence n'est pas dans la liste, dis honnêtement que tu apprends vite.
3. Adapte la langue : Si on te parle en anglais, réponds en anglais.
4. Si on te salue, présente-toi brièvement.
"""

# 6. GESTION DE L'HISTORIQUE
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": instruction_systeme}]

# 7. AFFICHAGE DU HEADER (IMAGE 3)
st.markdown("""
    <div class="header-box">
        <h1>Bonjour, je suis Serge Lionel LOKO</h1>
        <h3>N'hésitez pas à me poser des questions sur mon parcours et mes compétences.</h3>
    </div>
    """, unsafe_allow_html=True)

# Affichage des messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user", avatar="👤"):
            st.write(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant", avatar="💼"):
            st.write(msg["content"])

# 8. ZONE DE SAISIE ET GÉNÉRATION
if prompt := st.chat_input("Tapez vos questions..."):
    with st.chat_message("user", avatar="👤"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant", avatar="💼"):
        with st.spinner(""):
            try:
                reponse = client.chat.completions.create(
                    model="gpt-4o",
                    messages=st.session_state.messages
                )
                msg_ia = reponse.choices[0].message.content
                st.write(msg_ia)
                st.session_state.messages.append({"role": "assistant", "content": msg_ia})
            except Exception as e:
                st.error(f"Erreur : {e}")
