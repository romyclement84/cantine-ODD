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
<div class="header-card">
    <h1 style="margin:0; color:#1B5E20;">🍏 Objectif Zéro Gâchis au Collège</h1>
    <h3 style="margin-top:5px; color:#33691E;">Mesure et quantification — 700 demi-pensionnaires (Vaucluse)</h3>
    <p style="margin-bottom:0; margin-top:10px; color:#37474F;">
        Dans le cadre des <b>ODD (Objectifs de Développement Durable)</b>, notamment l'<b>ODD 12</b> (Consommation et production responsables), 
        découvrez l'impact en temps réel de notre restaurant scolaire.
    </p>
</div>
""", unsafe_allow_html=True)

# Calculs des totaux
total_nourriture = poids_alim + poids_pain + poids_fruits

# Préparation des données pour le graphique
donnees_du_jour = {
    "Catégorie": ["Déchets Alimentaires", "Pain", "Fruits Entamés", "Emballages", "Serviettes"],
    "Poids (kg)": [poids_alim, poids_pain, poids_fruits, poids_emb, poids_serviettes],
    "Couleur_Ref": ["#FB8C00", "#8D6E63", "#7CB342", "#039BE5", "#8E24AA"]
}
df_jour = pd.DataFrame(donnees_du_jour)

# Séparation en deux colonnes pour les résultats
col1, col2 = st.columns([1, 1.2])

with col1:
    # 1. Bloc Total Alerte Rouge
    st.markdown(f"""
    <div class="total-card">
        <h3 style="margin:0; color:#B71C1C; font-size:20px; letter-spacing: 1px;">⚠️ TOTAL NOURRITURE GASPILLÉE</h3>
        <p style="font-size:52px; font-weight:bold; margin:10px 0; color:#D32F2F;">{total_nourriture:.2f} kg</p>
        <small style="color:#C62828; font-weight:bold;">Alerte repas + pain + fruits</small>
    </div>
    """, unsafe_allow_html=True)
    
    # 2. Tableau multicolore en relief
    st.markdown(f"""
    <div class="container-card">
        <h3 style="margin-top:0; margin-bottom:15px; color:#37474F; text-align:center;">📋 Zoom par type de déchet</h3>
        <div class="poubelle-ligne double-alim">
            <span>🍲 Déchets Alimentaires</span>
            <span class="valeur-texte">{poids_alim:.1f} kg</span>
        </div>
        <div class="poubelle-ligne double-pain">
            <span>🥖 Poubelle à Pain</span>
            <span class="valeur-texte">{poids_pain:.1f} kg</span>
        </div>
        <div class="poubelle-ligne double-fruits">
            <span>🍎 Fruits entamés</span>
            <span class="valeur-texte">{poids_fruits:.1f} kg</span>
        </div>
        <div class="poubelle-ligne double-emb">
            <span>📦 Emballages recyclables</span>
            <span class="valeur-texte">{poids_emb:.1f} kg</span>
        </div>
        <div class="poubelle-ligne double-serviettes">
            <span>🧻 Serviettes en papier</span>
            <span class="valeur-texte">{poids_serviettes:.1f} kg</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # 3. Bloc Graphique
    st.markdown('<div class="container-card" style="background-color: #ffffff; height: 100%;">', unsafe_allow_html=True)
    st.markdown('<h3 style="margin-top:0; color:#37474F; text-align:center;">📈 Visualisation Graphique</h3>', unsafe_allow_html=True)
    st.bar_chart(data=df_jour, x="Catégorie", y="Poids (kg)", color="Couleur_Ref")
    st.markdown('</div>', unsafe_allow_html=True)
