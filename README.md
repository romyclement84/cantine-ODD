<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Stop au Gaspillage - Saisie des Pesées</title>
  <style>
    /* Le CSS pour organiser notre page */
    body {
      font-family: Arial, sans-serif;
      display: flex; /* Permet de mettre la colonne et le contenu côte à côte */
      margin: 0;
      padding: 0;
      height: 100vh;
    }

    /* Styles pour la colonne de gauche */
    .colonne-gauche {
      width: 320px;
      background-color: #f4f6f7;
      padding: 20px;
      border-right: 2px solid #ddd;
    }

    /* Styles pour l'espace de droite */
    .espace-droite {
      flex: 1; /* Prend tout le reste de la place de l'écran */
      padding: 40px;
    }

    /* Espacement pour chaque bloc de déchet */
    .bloc-dechet {
      margin-bottom: 20px;
    }

    /* Style du texte au-dessus du rectangle */
    label {
      display: block;
      font-weight: bold;
      margin-bottom: 8px;
      color: #2c3e50;
    }

    /* Style de nos rectangles de saisie */
    input {
      width: 100%;
      padding: 10px;
      border: 2px solid #bdc3c7;
      border-radius: 6px;
      font-size: 14px;
      box-sizing: border-box; /* Évite que le rectangle dépasse */
    }

    /* Change la couleur du bord quand on clique dans le rectangle */
    input:focus {
      border-color: #27ae60;
      outline: none;
    }

    /* Un joli bouton pour enregistrer plus tard */
    .bouton-enregistrer {
      background-color: #27ae60;
      color: white;
      padding: 12px;
      border: none;
      border-radius: 6px;
      width: 100%;
      font-size: 16px;
      font-weight: bold;
      cursor: pointer;
      margin-top: 10px;
    }
  </style>
</head>
<body>

  <div class="colonne-gauche">
    <h2 style="color: #27ae60; margin-top: 0;">📊 Saisie des pesées</h2>
    <p style="font-size: 13px; color: #7f8c8d;">Entrez le poids en kg ou en grammes.</p>

    <div class="bloc-dechet">
      <label>🥖 Poubelle à Pain</label>
      <input type="text" placeholder="Ex: 4.5 kg ou 4500 g">
    </div>

    <div class="bloc-dechet">
      <label>🍎 Déchets Alimentaires</label>
      <input type="text" placeholder="Ex: 12.3 kg">
    </div>

    <div class="bloc-dechet">
      <label>📦 Emballages</label>
      <input type="text" placeholder="Ex: 800 g">
    </div>

    <div class="bloc-dechet">
      <label>🍏 Fruits entamés</label>
      <input type="text" placeholder="Ex: 1.2 kg">
    </div>

    <div class="bloc-dechet">
      <label>🧻 Serviettes papiers</label>
      <input type="text" placeholder="Ex: 500 g">
    </div>

    <button class="bouton-enregistrer">Valider la pesée</button>
  </div>

  <div class="espace-droite">
    <h1>🌿 Opération Cantine Éco-Responsable</h1>
    <h3>Collège du Vaucluse — 700 Demi-pensionnaires (ODD 12)</h3>
    
    <p style="font-size: 16px; margin-top: 40px; color: #555;">
      ← Utilisez la colonne de gauche pour enregistrer les pesées quotidiennes de la cantine.
    </p>
    <p>Bientôt, nous allons coder cette zone pour qu'elle affiche automatiquement des graphiques et des calculs (comme le total des déchets ou la moyenne de gaspillage par élève !).</p>
  </div>

</body>
</html>
