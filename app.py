import streamlit as st
import pandas as pd
import datetime

# 1. Configuration de la page
st.set_page_config(page_title="Cantine Durable - ODD", page_icon="🍏", layout="wide")

# Style CSS pour appliquer le relief (ombres) et le jaune pastel à TOUS les éléments
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
    
    /* Lignes de poubelles à l'intérieur de la carte jaune pastel */
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
# En-tête principal en relief
st.markdown("""
<div class="custom-card" style="background-color: #ffffff;">
    <h1 style="margin:0; color:#2E7D32;">🍏 Objectif Zéro Gâchis au Collège</h1>
    <h3 style="margin-top:5px; color:#558B2F;">Mesure et quantification — 700 demi-pensionnaires (Vaucluse)</h3>
    <p style="margin-bottom:0; margin-top:10px; color:#616161;">
        Dans le cadre des <b>ODD (Objectifs de Développement Durable)</b>, notamment l'<b>ODD 12</b> (Consommation et production responsables), 
        nous suivons au jour le jour l'impact de notre restaurant scolaire pour sensibiliser toute la communauté.
    </p>
</div>
""", unsafe_allow_html=True)

# Calculs des totaux
total_nourriture = poids_alim + poids_pain + poids_fruits

# Préparation des données pour le graphique
donnees_du_jour = {
    "Catégorie": ["Déchets Alimentaires", "Pain", "Fruits Entamés", "Emballages", "Serviettes"],
    "Poids (kg)": [poids_alim, poids_pain, poids_fruits, poids_emb, poids_serviettes]
}
df_jour = pd.DataFrame(donnees_du_jour)

# Séparation en deux colonnes pour les résultats
col1, col2 = st.columns([1, 1.2])

with col1:
    # 1. Bloc Total en gros relief jaune + écriture ROUGE vif
    st.markdown(f"""
    <div class="total-card">
        <h3 style="margin:0; color:#5D4037; font-size:18px;">TOTAL NOURRITURE GASPILLÉE</h3>
        <p style="font-size:46px; font-weight:bold; margin:10px 0; color:#D32F2F;">{total_nourriture:.2f} kg</p>
        <small style="color:#795548; font-weight:bold;">(Repas + Pain + Fruits)</small>
    </div>
    """, unsafe_allow_html=True)
    
    # 2. Tableau en relief et en jaune pastel (Détails par poubelle)
    st.markdown(f"""
    <div class="custom-card">
        <h3 style="margin-top:0; margin-bottom:15px; color:#5D4037; text-align:center;">📋 Détail par Poubelle</h3>
        <div class="poubelle-ligne">
            <span class="poubelle-titre">🍲 Déchets Alimentaires</span>
            <span class="poubelle-valeur">{poids_alim:.1f} kg</span>
        </div>
        <div class="poubelle-ligne">
            <span class="poubelle-titre">🥖 Poubelle à Pain</span>
            <span class="poubelle-valeur">{poids_pain:.1f} kg</span>
        </div>
        <div class="poubelle-ligne">
            <span class="poubelle-titre">🍎 Fruits entamés</span>
            <span class="poubelle-valeur">{poids_fruits:.1f} kg</span>
        </div>
        <div class="poubelle-ligne">
            <span class="poubelle-titre">📦 Emballages</span>
            <span class="poubelle-valeur">{poids_emb:.1f} kg</span>
        </div>
        <div class="poubelle-ligne">
            <span class="poubelle-titre">🧻 Serviettes en papier</span>
            <span class="poubelle-valeur">{poids_serviettes:.1f} kg</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # 3. Bloc Graphique également intégré dans une carte en relief
    st.markdown('<div class="custom-card" style="background-color: #ffffff; height: 100%;">', unsafe_allow_html=True)
    st.markdown('<h3 style="margin-top:0; color:#5D4037; text-align:center;">📈 Graphique des Déchets</h3>', unsafe_allow_html=True)
    st.bar_chart(data=df_jour, x="Catégorie", y="Poids (kg)", color="#FBC02D")
    st.markdown('</div>', unsafe_allow_html=True)
