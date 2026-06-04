import streamlit as st
import pandas as pd
import datetime

# 1. Configuration de la page
st.set_page_config(page_title="Cantine Durable - ODD", page_icon="🍏", layout="wide")

# Style CSS pour appliquer le relief (ombres) à TOUS les éléments
st.markdown("""
    <style>
    /* Style global pour toutes les cartes en relief */
    .custom-card {
        background-color: #FFFDE7; /* Jaune pastel très clair */
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1); /* Relief prononcé */
        border: 1px solid #FFF59D;
        margin-bottom: 20px;
    }
    
    /* Carte spéciale pour le total (jaune un peu plus soutenu) */
    .total-card {
        background-color: #FFF9C4; 
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.12); /* Gros relief pour le total */
        border: 1px solid #FFF59D;
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Lignes d'ingrédients/poubelles à l'intérieur de la carte */
    .poubelle-ligne {
        background-color: #ffffff;
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05); /* Petit relief interne */
        border-left: 5px solid #FBC02D;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .poubelle-titre {
        font-weight: bold;
        color: #5D4037;
    }
    
    .poubelle-valeur {
        font-size: 18px;
        font-weight: bold;
        color: #F57F17;
    }
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
    
    poids_alim = st.number_input("Déchets Alimentaires (en kg)", min_value=0.0, max_value=200.0, value=0.0, step=0.1)
    poids_pain = st.number_input("Pain gaspillé (en kg)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    poids_fruits = st.number_input("Fruits entamés (en kg)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    poids_emb = st.number_input("Emballages (en kg)", min_value=0.0, max_value=50.0, value=0.0, step=0.1)
    poids_serviettes = st.number_input("Serviettes papier (en kg)", min_value=0.0, max_value=50.0, value=0.0, step=0.1)

    st.success("Données mises à jour ! 🚀")


# ==========================================
# PAGE PRINCIPALE (À droite)
# ==========================================
# En-tête principal lui aussi dans une carte en relief
st.markdown("""
<div class="custom-card" style="background-color: #ffffff;">
    <h1 style="margin:0; color:#2E7D32;">🍏 Objectif Zéro Gâchis au Collège</h1>
    <h3
