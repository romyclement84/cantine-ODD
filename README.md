import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Eco-Cantine Vaucluse", page_icon="🍏", layout="centered")

# Titre principal
st.title("🍏 Stop au Gaspillage - Notre Cantine")
st.subheader("Collège du Vaucluse — 700 Demi-pensionnaires")
st.write("Aidez-nous à quantifier le gaspillage en enregistrant ce que vous jetez.")

st.divider() # Ligne de séparation

# Création du formulaire de saisie
st.header("📥 Enregistrer un déchet")

with st.form("formulaire_dechets"):
    
    # 1. Zone pour le Pain
    st.subheader("🥖 Le Pain")
    col1, col2 = st.columns(2)
    with col1:
        nb_pain = st.number_input("Nombre de morceaux de pain :", min_value=0, step=1, value=0)
    with col2:
        poids_pain = st.number_input("Poids estimé du pain (en grammes) :", min_value=0, step=5, value=0)

    st.divider()

    # 2. Zone pour les Fruits Entamés
    st.subheader("🍏 Fruits entamés")
    col3, col4 = st.columns(2)
    with col3:
        nb_fruits = st.number_input("Nombre de fruits entamés :", min_value=0, step=1, value=0)
    with col4:
        poids_fruits = st.number_input("Poids estimé des fruits (en grammes) :", min_value=0, step=5, value=0)

    st.divider()

    # 3. Zone pour les Serviettes en papier
    st.subheader("🧻 Serviettes en papier")
    col5, col6 = st.columns(2)
    with col5:
        nb_serviettes = st.number_input("Nombre de serviettes jetées :", min_value=0, step=1, value=0)
    with col6:
        poids_serviettes = st.number_input("Poids des serviettes (en grammes) :", min_value=0, step=1, value=0)

    st.divider()

    # 4. Zone pour les Emballages
    st.subheader("📦 Emballages")
    col7, col8 = st.columns(2)
    with col7:
        nb_emballages = st.number_input("Nombre d'emballages (pots de yaourt, plastique...) :", min_value=0, step=1, value=0)
    with col8:
        poids_emballages = st.number_input("Poids des emballages (en grammes) :", min_value=0, step=1, value=0)

    # Bouton de validation du formulaire
    bouton_valider = st.form_submit_button("Enregistrer les données")

# Ce qui se passe quand on clique sur le bouton
if bouton_valider:
    st.success("🎉 Merci ! Vos données ont bien été prises en compte pour l'analyse ODD.")
    
    # Affichage d'un récapitulatif pour l'utilisateur
    st.write("### Récapitulatif de votre saisie :")
    st.write(f"- **Pain :** {nb_pain} morceau(x) ({poids_pain}g)")
    st.write(f"- **Fruits :** {nb_fruits} fruit(s) ({poids_fruits}g)")
    st.write(f"- **Serviettes :** {nb_serviettes} serviette(s) ({poids_serviettes}g)")
    st.write(f"- **Emballages :** {nb_emballages} emballage(s) ({poids_emballages}g)")
    
