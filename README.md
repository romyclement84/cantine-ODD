<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Notre Cantine ODD</title>
  <style>
    /* Structure simple en deux colonnes */
    .conteneur {
      display: flex;
      font-family: sans-serif;
      padding: 20px;
    }

    /* La colonne de gauche pour les poubelles */
    .colonne-poubelles {
      width: 300px;
      background-color: #f5f5f5;
      padding: 20px;
      border-radius: 10px;
      margin-right: 30px;
    }

    /* L'espace de droite pour les résultats */
    .colonne-resultats {
      flex: 1;
    }

    /* Style des zones de texte (les rectangles) */
    .case-saisie {
      margin-bottom: 15px;
    }

    label {
      display: block;
      font-weight: bold;
      margin-bottom: 5px;
    }

    input {
      width: 100%;
      padding: 8px;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;
    }

    button {
      width: 100%;
      padding: 10px;
      background-color: #2e7d32;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-weight: bold;
    }
  </style>
</head>
<body>

  <div class="conteneur">

    <div class="colonne-poubelles">
      <h2>Saisie du Tri</h2>
      
      <div class="case-saisie">
        <label>🥖 Poubelle à Pain</label>
        <input type="text" placeholder="Ex: 4 kg">
      </div>

      <div class="case-saisie">
        <label>🍎 Déchets Alimentaires</label>
        <input type="text" placeholder="Ex: 15 kg">
      </div>

      <div class="case-saisie">
        <label>📦 Emballages</label>
        <input type="text" placeholder="Ex: 2 kg">
      </div>

      <div class="case-saisie">
        <label>🍏 Fruits Entamés</label>
        <input type="text" placeholder="Ex: 1 kg">
      </div>

      <div class="case-saisie">
        <label>🧻 Serviettes Papiers</label>
        <input type="text" placeholder="Ex: 0.5 kg">
      </div>

      <button>Calculer le gaspillage</button>
    </div>

    <div class="colonne-resultats">
      <h1>Collège du Vaucluse - Objectif ODD 12</h1>
      <p>Suivi de la production de déchets pour 700 demi-pensionnaires.</p>
      <hr>
      <p><em>Les résultats s'afficheront ici dès que nous aurons ajouté le code de calcul.</em></p>
    </div>

  </div>

</body>
</html>
