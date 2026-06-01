import streamlit as st

# 1. Configuration de la page
st.set_page_config(
    page_title="Eco-Cantine 84", 
    page_icon="♻️", 
    layout="centered"
)

# 2. Titre et Introduction (Objectifs ODD)
st.title("♻️ Mesure des Déchets - Notre Cantine")
st.write("### Collège du Vaucluse — 700 Demi-pensionnaires")
st.write("Ce site nous aide à mesurer notre impact pour l'ODD 12 (Consommation responsable).")

st.info("Remplissez les cases ci-dessous selon ce que vous allez jeter dans les poubelles de tri.")

# 3. Formulaire de saisie pour les élèves / le personnel
with st.form("formulaire_dechets_cantine"):
    
    # --- POUBELLE 1 : LE PAIN ---
    st.markdown("### 🥖 Poubelle : PAIN")
    qte_pain = st.number_input("Nombre de morceaux de pain jetés :", min_value=0, step=1, value=0)
    poids_pain = st.number_input("Poids du pain jeté (en grammes) :", min_value=0, step=10, value=0)
    
    st.write("---") # Ligne de séparation
    
    # --- POUBELLE 2 : FRUITS ENTAMÉS ---
    st.markdown("### 🍏 Poubelle : FRUITS ENTAMÉS")
    qte_fruits = st.number_input("Nombre de fruits entamés jetés :", min_value=0, step=1, value=0)
    poids_fruits = st.number_input("Poids des fruits jetés (en grammes) :", min_value=0, step=10, value=0)
    
    st.write("---")
    
    # --- POUBELLE 3 : SERVIETTES EN PAPIER ---
    st.markdown("### 🧻 Poubelle : SERVIETTES EN PAPIER")
    qte_serviettes = st.number_input("Nombre de serviettes jetées :", min_value=0, step=1, value=0)
    poids_serviettes = st.number_input("Poids des serviettes jetées (en grammes) :", min_value=0, step=1, value=0)
    
    st.write("---")
    
    # --- POUBELLE 4 : EMBALLAGES ---
    st.markdown("### 📦 Poubelle : EMBALLAGES")
    qte_emballages = st.number_input("Nombre d'emballages jetés (pots, plastiques...) :", min_value=0, step=1, value=0)
    poids_emballages = st.number_input("Poids des emballages jetés (en grammes) :", min_value=0, step=1, value=0)
    
    # --- BOUTON DE VALIDATION ---
    bouton_valider = st.form_submit_button("Enregistrer ma poubelle")

# 4. Traitement des données après le clic sur le bouton
if bouton_valider:
    st.success("🎉 Merci ! Vos données ont été enregistrées pour le projet ODD du collège.")
    
    # Affichage du récapitulatif des données saisies
    st.write("#### 📊 Récapitulatif de votre saisie :")
    
    # Création d'un petit tableau propre pour afficher le résultat
    st.columns(4)
    st.write(f"• **Pain :** {qte_pain} morceau(x) jeté(s) soit **{poids_pain}g**")
    st.write(f"• **Fruits :** {qte_fruits} fruit(s) jeté(s) soit **{poids_fruits}g**")
    st.write(f"• **Serviettes :** {qte_serviettes} serviette(s) jetée(s) soit **{poids_serviettes}g**")
    st.write(f"• **Emballages :** {qte_emballages} emballage(s) jeté(s) soit **{poids_emballages}g**")
