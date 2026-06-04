import streamlit as st
import pandas as pd
import datetime
import plotly.express as px

# 1. Configuration de la page
st.set_page_config(page_title="Cantine Durable - ODD", page_icon="🍏", layout="wide")

# NOM DE VOTRE FICHIER IMAGE IMPORTÉ SUR GITHUB
# (Assurez-vous de renommer votre image "college.jpg" sur GitHub ou de changer ce nom ici)
NOM_IMAGE_FOND = "college.jpg" 

# Injection du CSS pour le fond d'écran et la transparence des cartes
st.markdown(f"""
    <style>
    /* Application de l'image de fond locale sur tout le site */
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.75), rgba(255, 255, 255, 0.75)), url("app/static/{NOM_IMAGE_FOND}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Blocs légèrement transparents pour voir le collège en arrière-plan */
    .header-card {{
        background: linear-gradient(135deg, rgba(232, 245, 233, 0.9), rgba(200, 230, 201, 0.9));
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        border: 1px solid #A5D6A7;
        margin-bottom: 20px;
    }}
    
    .container-card {{
        background-color: rgba(250, 250, 250, 0.9);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.12);
        border: 1px solid #E0E0E0;
        margin-bottom: 20px;
    }}
    
    .total-card {{
        background: linear-gradient(135deg, rgba(255, 235, 235, 0.95), rgba(255, 205, 210, 0.95));
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(211, 47, 47, 0.2);
        border: 2px solid #EF9A9A;
        text-align: center;
        margin-bottom: 20px;
    }}
    
    .poubelle-ligne {{
        padding: 14px;
        border-radius: 10px;
        margin-bottom: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-weight: bold;
    }}
    .double-alim {{ background-color: rgba(255, 224, 178, 0.9); border-left: 6px solid #FB8C00; color: #E65100; }}
    .double-pain {{ background-color: rgba(215, 204, 200, 0.9); border-left: 6px solid #8D6E63; color: #4E342E; }}
    .double-fruits {{ background-color: rgba(220, 237, 200, 0.9); border-left: 6px solid #7CB342; color: #33691E; }}
    .double-emb {{ background-color: rgba(179, 229, 252, 0.9); border-left: 6px solid #039BE5; color: #01579B; }}
    .double-serviettes {{ background-color: rgba(225, 190, 231, 0.9); border-left: 6px solid #8E24AA; color: #4A148C; }}
    .valeur-texte {{ font-size: 20px; font-weight: bold; }}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# COLONNE DE GAUCHE : Saisie des données
# ==========================================
with st.sidebar:
    st.header("📝 Saisie des Pesées")
    st.write("Entrez les poids mesurés aujourd'hui :")
    
    date_saisie = st.date_input("Date de la pesée", datetime.date.today())
    st.markdown("---")
    
    poids_alim = st.number_input("🍲 Déchets Alimentaires (kg)", min_value=0.0, max_value=200.0, value=0.0, step=0.1)
    poids_pain = st.number_input("🥖 Pain gaspillé (kg)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    poids_fruits = st.number_input("🍎 Fruits entamés (kg)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    poids_emb = st.number_input("📦 Emballages (kg)", min_value=0.0, max_value=50.0, value=0.0, step=0.1)
    poids_serviettes = st.number_input("🧻 Serviettes papier (kg)", min_value=0.0, max_value=50.0, value=0.0, step=0.1)

    st.success("Données synchronisées ! 🚀")

# ==========================================
# PAGE PRINCIPALE : Partie supérieure
# ==========================================
st.markdown("""
<div class="header-card">
    <h1 style="margin:0; color:#1B5E20;">🍏 Objectif Zéro Gâchis au Collège</h1>
    <h3 style="margin-top:5px; color:#33691E;">Mesure et quantification — 700 demi-pensionnaires (Vaucluse)</h3>
    <p style="margin-bottom:0; margin-top:10px; color:#37474F;">
        Dans le cadre des <b>ODD (Objectifs de Développement Durable)</b>, notamment l'<b>ODD 12</b> (Consommation et production responsables), 
        découvrez l'impact en temps réel de notre restaurant scolaire.
    </p>
</div>
""", unsafe_allow_html=True)

total_nourriture = poids_alim + poids_pain + poids_fruits

# Préparation du tableau de données
df_jour = pd.DataFrame({
    "Catégorie": ["Déchets Alimentaires", "Pain", "Fruits Entamés", "Emballages", "Serviettes"], 
    "Poids (kg)": [poids_alim, poids_pain, poids_fruits, poids_emb, poids_serviettes]
})

# Dictionnaire de correspondance exacte des couleurs pour le graphique Plotly
palette_couleurs = {
    "Déchets Alimentaires": "#FB8C00",   # Orange
    "Pain": "#8D6E63",                  # Marron
    "Fruits Entamés": "#7CB342",        # Vert
    "Emballages": "#039BE5",            # Bleu
    "Serviettes": "#8E24AA"             # Violet
}

col1, col2 = st.columns([1, 1.2])

with col1:
    # 1. Total Rouge
    st.markdown(f'<div class="total-card"><h3 style="margin:0; color:#B71C1C; font-size:20px;">⚠️ TOTAL NOURRITURE GASPILLÉE</h3><p style="font-size:52px; font-weight:bold; margin:10px 0; color:#D32F2F;">{total_nourriture:.2f} kg</p><small style="color:#C62828; font-weight:bold;">Alerte repas + pain + fruits</small></div>', unsafe_allow_html=True)
    
    # 2. Tableau multicolore
    st.markdown('<div class="container-card"><h3 style="margin-top:0; margin-bottom:15px; color:#37474F; text-align:center;">📋 Zoom par type de déchet</h3><div class="poubelle-ligne double-alim"><span>🍲 Déchets Alimentaires</span><span class="valeur-texte">' + f'{poids_alim:.1f}' + ' kg</span></div><div class="poubelle-ligne double-pain"><span>🥖 Poubelle à Pain</span><span class="valeur-texte">' + f'{poids_pain:.1f}' + ' kg</span></div><div class="poubelle-ligne double-fruits"><span>🍎 Fruits entamés</span><span class="valeur-texte">' + f'{poids_fruits:.1f}' + ' kg</span></div><div class="poubelle-ligne double-emb"><span>📦 Emballages recyclables</span><span class="valeur-texte">' + f'{poids_emb:.1f}' + ' kg</span></div><div class="poubelle-ligne double-serviettes"><span>🧻 Serviettes en papier</span><span class="valeur-texte">' + f'{poids_serviettes:.1f}' + ' kg</span></div></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="container-card" style="background-color: rgba(255,255,255,0.9); height: 100%;">', unsafe_allow_html=True)
    st.markdown('<h3 style="margin-top:0; color:#37474F; text-align:center;">📈 Visualisation Graphique</h3>', unsafe_allow_html=True)
    
    # Création du graphique Plotly avec l'association stricte des couleurs demandées
    fig = px.bar(
        df_jour, 
        x="Catégorie", 
        y="Poids (kg)", 
        color="Catégorie", 
        color_discrete_map=palette_couleurs
    )
    
    # Mise en page épurée
    fig.update_layout(
        showlegend=False,
        margin=dict(l=20, r=20, t=10, b=20),
        xaxis_title="",
        yaxis_title="Poids (en kg)",
        height=340,
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# RE
