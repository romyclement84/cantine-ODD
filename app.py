import streamlit as st
import pandas as pd
import datetime

# 1. Configuration de la page
st.set_page_config(page_title="Cantine Durable - ODD", page_icon="🍏", layout="wide")

# ==========================================
# COLONNE DE GAUCHE : Saisie des données
# ==========================================
with st.sidebar:
    st.header("📝 Saisie des Pesées")
    st.write("Entrez les poids mesurés aujourd'hui :")
    
    # Choix de la date (par défaut aujourd'hui)
    date_saisie = st.date_input("Date de la pesée", datetime.date.today())
    
    st.markdown("---") # Ligne de séparation
    
    # 1. Poubelle Déchets Alimentaires
    poids_alim = st.number_input(
        label="Déchets Alimentaires (en kg)", 
        min_value=0.0, 
        max_value=200.0, 
        value=0.0, 
        step=0.1,
        help="Reste des assiettes (hors pain et fruits)"
    )
    
    # 2. Poubelle Pain
    poids_pain = st.number_input(
        label="Pain gaspillé (en kg)", 
        min_value=0.0, 
        max_value=100.0, 
        value=0.0, 
        step=0.1
    )
    
    # 3. Poubelle Fruits Entamés
    poids_fruits = st.number_input(
        label="Fruits entamés (en kg)", 
        min_value=0.0, 
        max_value=100.0, 
        value=0.0, 
        step=0.1
    )
    
    # 4. Poubelle Emballages
    poids_emb = st.number_input(
        label="Emballages (en kg)", 
        min_value=0.0, 
        max_value=50.0, 
        value=0.0, 
        step=0.1
    )
    
    # 5. Poubelle Serviettes Papier
    poids_serviettes = st.number_input(
        label="Serviettes papier (en kg)", 
        min_value=0.0, 
        max_value=50.0, 
        value=0.0, 
        step=0.1
    )

    # Bouton pour valider (optionnel visuellement pour l'instant)
    st.success("Données prises en compte à droite ! 🚀")


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

# Création d'un dictionnaire avec les données saisies à gauche pour les afficher directement
donnees_du_jour = {
    "Catégorie de Poubelle": ["Déchets Alimentaires", "Pain", "Fruits Entamés", "Emballages", "Serviettes Papier"],
    "Poids Saisi (kg)": [poids_alim, poids_pain, poids_fruits, poids_emb, poids_serviettes]
}
df_jour = pd.DataFrame(donnees_du_jour)

# Affichage des résultats en direct
col1, col2 = st.columns(2)

with col1:
    st.header("📊 Chiffres de la saisie actuelle")
    # Calcul du total de nourriture (Alim + Pain + Fruits)
    total_nourriture = poids_alim + poids_pain + poids_fruits
    st.metric(label="Total Nourriture Gaspillée (Aujourd'hui)", value=f"{total_nourriture:.2f} kg")
    
    # Tableau récapitulatif
    st.dataframe(df_jour, use_container_width=True, hide_index=True)

with col2:
    st.header("📈 Répartition des déchets")
    # Graphique en barres des données saisies à gauche
    st.bar_chart(data=df_jour, x="Catégorie de Poubelle", y="Poids Saisi (kg)")
