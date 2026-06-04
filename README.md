import streamlit as st
import pandas as pd

# 1. Configuration de la page
st.set_page_config(page_title="Cantine Durable - ODD", page_icon="🍏", layout="wide")

# 2. Titre principal
st.title("🍏 Objectif Zéro Gâchis au Collège")
st.subheader("Mesure et quantification des déchets de notre cantine (Vaucluse)")

# 3. Introduction et lien avec les ODD
st.markdown("""
Chaque jour, notre collège accueille **700 demi-pensionnaires**. Dans le cadre des **ODD (Objectifs de Développement Durable)**, 
notre objectif est de réduire le gaspillage alimentaire (ODD 12 : Consommation et production responsables).
""")

# 4. Chargement des données (le fichier CSV)
try:
    df = pd.read_csv("donnees_cantine.csv")
    
    # Affichage des chiffres clés
    st.header("📊 Nos Chiffres Clés")
    
    # Calcul des totaux
    total_nourriture = df["Dechets_Alimentaires"].sum() + df["Pain"].sum() + df["Fruits_Entames"].sum()
    st.metric(label="Total Nourriture Gaspillée (kg)", value=f"{total_nourriture:.1f} kg")
    
    # Affichage du graphique
    st.header("📈 Évolution des déchets sur la semaine")
    st.line_chart(df.set_index("Date"))
    
    # Affichage du tableau brut pour transparence
    st.header("📋 Données brutes")
    st.dataframe(df)

except Exception as e:
    st.warning("En attente de l'importation du fichier 'donnees_cantine.csv' ou vérification du format.")
