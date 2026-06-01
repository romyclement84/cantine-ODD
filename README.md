import streamlit as st

# Configuration de l'application
st.set_page_config(page_title="Eco-Cantine", page_icon="🍏")

st.title("🍏 Suivi des Déchets - Notre Cantine")
st.write("Aidez le collège à quantifier le gaspillage pour les ODD !")

# Formulaire simplifié
with st.form("formulaire_cantine"):
    st.subheader("🥖 Le Pain")
    nb_pain = st.number_input("Nombre de morceaux de pain :", min_value=0, step=1)
    poids_pain = st.number_input("Poids du pain (en grammes) :", min_value=0, step=5)

    st.subheader("🍏 Fruits entamés")
    nb_fruits = st.number_input("Nombre de fruits entamés :", min_value=0, step=1)
    poids_fruits = st.number_input("Poids des fruits (en grammes) :", min_value=0, step=5)

    st.subheader("🧻 Serviettes en papier")
    nb_serviettes = st.number_input("Nombre de serviettes :", min_value=0, step=1)
    poids_serviettes = st.number_input("Poids des serviettes (en grammes) :", min_value=0, step=1)

    st.subheader("📦 Emballages")
    nb_emballages = st.number_input("Nombre d'emballages :", min_value=0, step=1)
    poids_emballages = st.number_input("Poids des emballages (en grammes) :", min_value=0, step=1)

    # Bouton magique
    bouton = st.form_submit_button("Enregistrer ma poubelle")

# Action après clic
if bouton:
    st.success("✅ Données enregistrées avec succès ! Merci pour votre geste éco-citoyen.")
    st.write(f"**Récapitulatif :** Pain ({nb_pain} pcs / {poids_pain}g) | Fruits ({nb_fruits} pcs / {poids_fruits}g) | Serviettes ({nb_serviettes} pcs / {poids_serviettes}g) | Emballages ({nb_emballages} pcs / {poids_emballages}g)")
