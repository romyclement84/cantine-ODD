<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Suivi Déchets - Collège du Vaucluse</title>
  <style>
    /* Styles pour forcer l'affichage en deux colonnes */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
      background-color: #f9f9f9;
    }
    
    .titre-principal {
      text-align: center;
      color: #2e7d32;
      margin-bottom: 30px;
    }

    .conteneur-principal {
      display: flex;
      gap: 40px; /* Espace entre les deux colonnes */
      max-width: 1100px;
      margin: 0 auto;
    }

    /* Colonne Gauche (Formulaire) */
    .colonne-saisie {
      flex: 1;
      background-color: #ffffff;
      padding: 25px;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    /* Colonne Droite (Tableau des données) */
    .colonne-affichage {
      flex: 1;
      background-color: #ffffff;
      padding: 25px;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .groupe-poubelle {
      margin-bottom: 15px;
    }

    label {
      display: block;
      font-weight: bold;
      margin-bottom: 5px;
      color: #333;
    }

    input {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;
      font-size: 14px;
    }

    /* Style du tableau à droite */
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 15px;
    }

    th, td {
      border: 1px solid #ddd;
      padding: 12px;
      text-align: left;
    }

    th {
      background-color: #4caf50;
      color: white;
    }

    tr:nth-child(even) {
      background-color: #f2f2f2;
    }
  </style>
</head>
<body>

  <h1 class="titre-principal">🌿 ODD 12 : Quantification des Déchets de la Cantine</h1>
  <p style="text-align: center; color: #555;">Collège du Vaucluse — Suivi pour 700 demi-pensionnaires</p>

  <div class="conteneur-principal">

    <div class="colonne-saisie">
      <h2 style="color: #2e7d32; margin-top: 0;">1. Enregistrer les poids</h2>
      
      <div class="groupe-poubelle">
        <label>🥖 Poubelle à Pain</label>
        <input type="text" placeholder="Entrez le poids (ex: 5 kg)...">
      </div>

      <div class="groupe-poubelle">
        <label>🍎 Déchets Alimentaires</label>
        <input type="text" placeholder="Entrez le poids (ex: 18 kg)...">
      </div>

      <div class="groupe-poubelle">
        <label>📦 Emballages</label>
        <input type="text" placeholder="Entrez le poids (ex: 3 kg)...">
      </div>

      <div class="groupe-poubelle">
        <label>🍏 Fruits Entamés</label>
        <input type="text" placeholder="Entrez le poids (ex: 2.5 kg)...">
      </div>

      <div class="groupe-poubelle">
        <label>🧻 Serviettes Papiers</label>
        <input type="text" placeholder="Entrez le poids (ex: 1 kg)...">
      </div>
    </div>

    <div class="colonne-affichage">
      <h2 style="color: #2e7d32; margin-top: 0;">2. Données enregistrées</h2>
      <p style="font-size: 14px; color: #666;">Voici le récapitulatif des catégories suivies dans le collège :</p>
      
      <table>
        <thead>
          <tr>
            <th>Poubelle / Catégorie</th>
            <th>Poids mesuré</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>🥖 Poubelle à Pain</strong></td>
            <td>---</td>
          </tr>
          <tr>
            <td><strong>🍎 Déchets Alimentaires</strong></td>
            <td>---</td>
          </tr>
          <tr>
            <td><strong>📦 Emballages</strong></td>
            <td>---</td>
          </tr>
          <tr>
            <td><strong>🍏 Fruits Entamés</strong></td>
            <td>---</td>
          </tr>
          <tr>
            <td><strong>🧻 Serviettes Papiers</strong></td>
            <td>---</td>
          </tr>
        </tbody>
      </table>
    </div>

  </div>

</body>
</html>
