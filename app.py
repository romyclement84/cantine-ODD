import streamlit as st
import pandas as pd
import datetime

# 1. Configuration de la page
st.set_page_config(page_title="Cantine Durable - ODD", page_icon="🍏", layout="wide")

# Style CSS pour un festival de couleurs en relief
st.markdown("""
    <style>
    /* Cartes principales */
    .header-card {
        background: linear-gradient(135deg, #E8F5E9, #C8E6C9); /* Dégradé vert nature */
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        border: 1px solid #A5D6A7;
        margin-bottom: 20px;
    }
    
    .container-card {
        background-color: #FAFAFA;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.08);
        border: 1px solid #E0E0E0;
        margin-bottom: 20px;
    }
    
    /* Carte Rouge Flash pour le Total */
    .total-card {
        background: linear-gradient(135deg, #FFEBEE, #FFCDD2); /* Dégradé rouge clair */
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(211, 47, 47, 0.2); /* Ombre teintée rouge */
        border: 2px solid #EF9A9A;
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* ---- COULEURS INDIVIDUELLES DES POUBELLES (En relief) ---- */
    .poubelle-ligne {
        padding: 14px;
        border-radius: 10px;
        margin-bottom: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-weight: bold;
        transition: transform 0.2s;
    }
    
    /* 1. Déchets alimentaires = Orange doux */
    .double-alim {
        background-color: #FFE0B2; 
        border-left: 6px solid #FB8C00;
        color: #E65100;
    }
    /* 2. Pain = Marron clair */
    .double-pain {
        background-color: #D7CCC8; 
        border-left: 6px solid #8D6E63;
        color: #4E342E;
    }
    /* 3. Fruits = Vert pomme */
    .double-fruits {
        background-color: #DCEDC8; 
        border-left: 6px solid #7CB342;
        color: #33691E;
    }
    /* 4. Emballages = Bleu ciel */
    .double-emb {
        background-color: #B3E5FC; 
        border-left: 6px solid #039BE5;
        color: #01579B;
    }
    /* 5. Serviettes = Violet très doux */
    .double-serviettes {
        background-color: #E1BEE7; 
        border-left: 6px solid #8E24AA;
        color: #4A148C;
    }

    .valeur-texte {
        font-size: 20px;
        font-weight: bold;
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
    
    poids_alim = st.number_input("🍲 Déchets Alimentaires (kg)", min_value=0.0, max_value=200.0, value=0.0, step=0.1)
    poids_pain = st.number_input("🥖 Pain gaspillé (kg)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    poids_fruits = st.number_input("🍎 Fruits entamés (kg)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    poids_emb = st.number_input("📦 Emballages (kg)", min_value=0.0, max_value=50.0, value=0.0, step=0.1)
    poids_serviettes = st.number_input("🧻 Serviettes papier (kg)", min_value=0.0, max_value=50.0, value=0.0, step=0.1)

    st.success("Données synchronisées ! 🚀")


# ==========================================
# PAGE PRINCIPALE (À droite)
# ==========================================
# En-tête principal avec un dégradé vert éco
st.markdown("""
