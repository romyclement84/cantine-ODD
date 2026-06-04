import streamlit as st
import pandas as pd
import datetime

# 1. Configuration de la page
st.set_page_config(page_title="Cantine Durable - ODD", page_icon="🍏", layout="wide")

# Style CSS personnalisé pour le relief et le jaune pastel
st.markdown("""
    <style>
    /* Style pour la grande carte du score total */
    .total-card {
        background-color: #FFF9C4; /* Jaune pastel */
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Effet d'ombre/relief */
        border: 1px solid #FFF59D;
        text-align: center;
        margin-bottom: 25px;
    }
    /* Style pour les petites fiches de chaque poubelle */
    .poubelle-card {
        background-color: #FFFDE7; /* Jaune pastel très clair */
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05); /* Léger relief */
        border-left: 5px solid #FBC02D; /* Barre jaune plus foncée sur le côté */
        margin-bottom: 12px;
    }
    .poubelle-titre {
        font-weight: bold;
        color: #5D4037;
        margin-bottom: 2px;
    }
    .poubelle-valeur {
        font-size: 20px;
        font-weight: bold;
        color: #F57F17;
    }
    </style>
""", unsafe_index=False, unsafe_allow_html=True)


# ==========================================
# COLONNE DE GAUCHE : Saisie des données
# ==========================================
with st.sidebar:
    st.header("📝 Saisie des Pesées")
    st.write("Entrez les poids mesurés aujourd'hui :")
    
    date_saisie = st.date_input("Date de la pesée", datetime.date.today())
    st.markdown("---")
    
    poids_alim = st.number_input("Déchets Alimentaires (en kg)", min_value=0.0, max_value=200.0, value=0.0, step=0.1)
    poids_pain = st.number_input("Pain gaspillé (en kg)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    poids_fruits = st.number_input("Fruits entamés (en kg)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    poids_emb = st.number_input("Emballages (en kg)", min_value=0.0, max_value=50.0, value=0.0, step=0.1)
    poids_serviettes = st.number_input("Serviettes papier (en kg)", min_value=0.0, max_value=50.0, value=0.0, step=0.1)

    st.success("Données mises à jour ! 🚀")


# ==========================================
# PAGE PRINCIPALE (À droite)
# ==========================================
st.title("🍏 Objectif Zéro Gâchis au Collège")
st.subheader("Mesure et quantification des déchets de notre cantine (700 demi-pensionnaires)")

st.markdown("""
Dans le cadre des **ODD (Objectifs de Développement Durable)**, notamment l'**ODD 12** (Consommation et production responsables), 
nous suivons au jour le jour l'impact de notre restaurant scolaire.
""")

st.write("---")

# Calculs des totaux
total_nourriture = poids_alim + poids_pain + poids_fruits
total_autres = poids_emb + poids_serviettes

# Préparation des données pour le graphique
donnees_du_jour = {
    "Catégorie": ["Déchets Alimentaires", "Pain", "Fruits Entamés", "Emballages", "Serviettes"],
    "Poids (kg)": [poids_alim, poids_pain, poids_fruits, poids_emb, poids_serviettes]
}
df_jour = pd.DataFrame(donnees_du_jour)

# Affichage des résultats en direct
col1, col2 = st.columns([1, 1.2]) # La colonne du graphique est légèrement plus large

with col1:
    st.header("📊 Résumé des Pesées")
    
    # Grand encadré en relief jaune pour le total
    st.markdown(f"""
    <div class="total-card">
        <h3 style="margin:0; color:#5D4037;">Total Nourriture Gaspillée</h3>
        <p style="font-size:36px; font-weight:bold; margin:10px 0; color:#E65100;">{total_nourriture:.2f} kg</p>
        <small style="color:#795548;">(Repas + Pain + Fruits)</small>
    </div>
    """, unsafe_allow_html=True)
    
    # Liste des poubelles en relief jaune pastel
    st.markdown(f"""
    <div class="poubelle-card">
        <div class="poubelle-titre">🍲 Déchets Alimentaires (assiettes)</div>
        <div class="poubelle-valeur">{poids_alim:.1f} kg</div>
    </div>
    <div class="poubelle-card">
        <div class="poubelle-titre">🥖 Poubelle à Pain</div>
        <div class="poubelle-valeur">{poids_pain:.1f} kg</div>
    </div>
    <div class="poubelle-card">
        <div class="poubelle-titre">🍎 Fruits entamés</div>
        <div class="poubelle-valeur">{poids_fruits:.1f} kg</div>
    </div>
    <div class="poubelle-card">
        <div class="poubelle-titre">📦 Emballages</div>
        <div class="poubelle-valeur">{poids_emb:.1f} kg</div>
    </div>
    <div class="poubelle-card">
        <div class="poubelle-titre">🧻 Serviettes en papier</div>
        <div class="poubelle-valeur">{poids_serviettes:.1f} kg</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.header("📈 Visualisation")
    # Graphique en barres
    st.bar_chart(data=df_jour, x="Catégorie", y="Poids (kg)", color="#FBC02D") # Barres jaunes/dorées pour s'accorder au thème
