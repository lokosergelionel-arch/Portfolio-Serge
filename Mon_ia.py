import streamlit as st
from openai import OpenAI

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="Serge Lionel LOKO",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. CSS PROFESSIONNEL (Zéro Rouge, Zéro Logo Streamlit)
style_pro = """
    <style>
    /* Masquer tous les éléments natifs Streamlit (Menu, Header, Footer, Badge) */
    header, footer, #MainMenu, .stDeployButton, [data-testid="stHeader"] {
        visibility: hidden !important;
        display: none !important;
    }

    /* Supprimer l'espace blanc en haut */
    .stApp {
        margin-top: -60px;
    }

    /* CADRE DU HEADER (Design Image 3) */
    .header-container {
        border: 2px solid #0E2A47;
        border-radius: 12px;
        padding: 40px 25px;
        text-align: center;
        background-color: #FFFFFF;
        margin-bottom: 40px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .header-container h1 {
        color: #0E2A47 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 700;
        font-size: 28px;
        margin-bottom: 12px;
    }
    .header-container p {
        color: #4A4A4A !important;
        font-size: 16px;
        font-weight: 400;
    }

    /* CUSTOMISATION DU CHAT INPUT (Suppression du rouge) */
    /* Bordure au focus - On force le bleu marine */
    .stChatInput:focus-within {
        border-color: #0E2A47 !important;
    }

    /* Icône d'envoi (Avion) en bleu marine */
    button[data-testid="stChatInputSubmitButton"] svg {
        fill: #0E2A47 !important;
    }

    /* Avatar pro : Fond blanc pour les icônes */
    [data-testid="stChatMessage"] {
        background-color: transparent !important;
    }

    /* Ajustement Mobile pour que le cadre ne soit pas trop grand */
    @media (max-width: 640px) {
        .header-container h1 { font-size: 22px; }
        .header-container { padding: 25px 15px; }
        .stApp { margin-top: -40px; }
    }
    </style>
"""
st.markdown(style_pro, unsafe_allow_html=True)

# 3. CONFIGURATION API
try:
    api_key = st.secrets["OPENAI_API_KEY"]
except:
    st.error("Erreur : La clé OPENAI_API_KEY est manquante dans les secrets.")
    st.stop()

client = OpenAI(api_key=api_key)

# 4. TEXTE DE RÉFÉRENCE (PROFIL COMPLET)
profil_complet = """
IDENTITÉ :
- Nom : Serge Lionel LOKO
PROFIL : Service Desk Analyst (L1) | L2 Exposure | User Support Analyst | Chef de Projet | Développeur Junior

RÉSUMÉ :
Je possède un parcours atypique et complémentaire, alliant compétences humaines et techniques. Issu d’une formation initiale en germanistique, j’ai développé de solides capacités de communication, d’analyse et une forte sensibilité interculturelle.
En parallèle, j’ai acquis plus de quatre années d’expérience au sein de l’une des plus grandes organisations de jeunesse au monde AIESEC.
Guidé par une passion profonde pour la technologie, je me suis naturellement orienté vers l’informatique. Rigoureux, organisé et orienté solutions, j’apprends rapidement.

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
2. Customer Support Associate – Amazon | Majorel, Togo (2020)
3. German Customer Support – Level 3 | TCS | Hyderabad, India (2018–2019)

EDUCATION:
- Autodidacte en Intelligence Artificielle (2025)
- BSc in Data Science and Analytics | JAIN University, India (2024)
- Bachelor’s Degree – German Studies | University of Lomé (2018)

TOOLS : ServiceNow (SNOW), SAP, Office 365, Teams, Jira.
"""

# 5. INSTRUCTIONS SYSTÈME (LE CERVEAU)
instruction_systeme = f"""
Tu n'es pas une IA générique. TU ES SERGE LIONEL LOKO.
Tu parles toujours à la première personne du singulier ("Je", "Mon", "Mes").
Réponds de manière concise, professionnelle et directe.
Voici ton parcours :
{profil_complet}

RÈGLES :
1. Si un recruteur te demande "Qui êtes-vous ?", présente-toi brièvement.
2. Ne t'invente pas de vie. Si une compétence n'est pas dans la liste, dis honnêtement que tu apprends vite.
3. Adapte la langue : Si on te parle en anglais, réponds en anglais.
4. Si on te salue, présente-toi brièvement.
"""

# 6. INITIALISATION DE LA MÉMOIRE
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": instruction_systeme}]

# 7. AFFICHAGE DU HEADER (Design Image 3)
st.markdown("""
    <div class="header-container">
        <h1>Bonjour, je suis Serge Lionel LOKO</h1>
        <p>N'hésitez pas à me poser des questions sur mon parcours et mes compétences.</p>
    </div>
    """, unsafe_allow_html=True)

# 8. AFFICHAGE DES MESSAGES
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user", avatar="👤"):
            st.write(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant", avatar="💼"):
            st.write(msg["content"])

# 9. ZONE DE SAISIE ET LOGIQUE IA
if prompt := st.chat_input("Tapez vos questions..."):
    # Affichage message utilisateur
    with st.chat_message("user", avatar="👤"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Réponse assistant
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
                st.error(f"Une erreur est survenue : {e}")