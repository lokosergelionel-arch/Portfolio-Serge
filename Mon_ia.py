import streamlit as st
from openai import OpenAI

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Serge Lionel LOKO", page_icon="💼", layout="centered")

# --- CSS SUPRÊME (NETTOYAGE + COULEURS BLEUES + FIX CERCLE) ---
css_hack = """
    <style>
    /* 1. MASQUER TOUTE LA MARQUE STREAMLIT */
    #MainMenu {visibility: hidden; display: none;}
    footer {visibility: hidden; display: none;}
    header {visibility: hidden; display: none;}
    [data-testid="stHeader"] {visibility: hidden; display: none;}
    [data-testid="stToolbar"] {visibility: hidden; display: none;}

    /* Cacher le bouton 'Hosted with Streamlit' */
    .viewerBadge_container__1QSob {display: none !important;}
    div[class^='viewerBadge_container'] {display: none !important;}

    /* Remonter le contenu */
    .stApp {
        background-color: white; 
        margin-top: -80px; 
    }

    /* 2. CHANGER LA COULEUR ROUGE EN BLEU MARINE */
    /* La zone de texte (Input) */
    .stChatInput textarea:focus {
        border-color: #0E2A47 !important;
        box-shadow: 0 0 0 1px #0E2A47 !important;
    }

    /* Le bouton 'Envoyer' */
    button[kind="primary"] {
        background-color: #F8F9FA !important;
        border: 1px solid #0E2A47 !important;
        color: #0E2A47 !important;
    }
    button[kind="primary"]:hover {
        background-color: #0E2A47 !important;
        color: white !important;
    }

    /* 3. DESIGN DU CADRE (HEADER) */
    .header-box {
        border: 2px solid #0E2A47;
        padding: 30px;
        border-radius: 12px;
        background-color: #F8F9FA;
        text-align: center;
        margin-bottom: 30px;
    }
    .header-box h1 { 
        color: #0E2A47 !important;
        font-family: 'Helvetica', sans-serif;
        font-size: 28px;
        margin-bottom: 10px; 
    }
    .header-box h3 { 
        color: #4A4A4A !important;
        font-size: 18px;
        font-weight: normal; 
    }

    /* J'AI SUPPRIMÉ LA LIGNE QUI CACHAIT LE CERCLE ICI */

    </style>
"""
st.markdown(css_hack, unsafe_allow_html=True)

# 2. CONNEXION OPENAI
try:
    api_key = st.secrets["OPENAI_API_KEY"]
except:
    st.error("Erreur : Clé API manquante.")
    st.stop()

client = OpenAI(api_key=api_key)

# 3. PROFIL COMPLET
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
- Collaboration with L2/L3 teams.

2. Customer Support Associate – Amazon | Majorel, Togo (2020)
- Support via phone/email, conflict management.

3. German Customer Support – Level 3 | TCS | Hyderabad, India (2018–2019)
- Level 3 support tickets, SAP usage, critical tickets management.

EDUCATION:
- Autodidacte en Intelligence Artificielle (2025)
- BSc in Data Science and Analytics | JAIN University, India (2024)
- Bachelor’s Degree – German Studies | University of Lomé (2018)

TOOLS : ServiceNow (SNOW), SAP, Office 365, Teams, Jira.

SOFT SKILLS :
- Curieux, résilient, très bon relationnel.
- Rigoureux, organisé, fiable.
- Esprit d’équipe.

CONTACT :
- Email : loko.sergelionel@gmail.com
- LinkedIn : https://www.linkedin.com/in/koffi-mawugnon-serge-lionel-loko
"""

# 4. LE CERVEAU
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
"""

# 5. AFFICHAGE HEADER
st.markdown("""
    <div class="header-box">
        <h1>Bonjour, je suis Serge Lionel LOKO</h1>
        <h3>N'hésitez pas à me poser des questions sur mon parcours et mes compétences.</h3>
    </div>
    """, unsafe_allow_html=True)

# 6. MÉMOIRE
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": instruction_systeme}]

# 7. DISCUSSION
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user", avatar="👤"):
            st.write(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant", avatar="💼"):
            st.write(msg["content"])

# 8. ZONE DE SAISIE AVEC LE CERCLE QUI TOURNE ENFIN !
if prompt := st.chat_input("Tapez vos questions..."):
    with st.chat_message("user", avatar="👤"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant", avatar="💼"):
        # Le cercle va tourner ici car j'ai enlevé le CSS qui le cachait
        with st.spinner(""):
            reponse = client.chat.completions.create(
                model="gpt-4o",
                messages=st.session_state.messages
            )
            msg_ia = reponse.choices[0].message.content
        st.write(msg_ia)

    st.session_state.messages.append({"role": "assistant", "content": msg_ia})