<style>
  body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f0f4f8;
  }
  
  .titre-site {
    text-align: center;
    color: #1b5e20;
    margin-bottom: 25px;
  }

  /* Création des deux colonnes côte à côte */
  .ecran-partage {
    display: flex;
    gap: 30px;
    max-width: 1200px;
    margin: 0 auto;
  }

  /* Colonne Gauche (Saisie) */
  .colonne-saisie {
    flex: 1;
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
  }

  /* Colonne Droite (Affichage des données) */
  .colonne-affichage {
    flex: 1;
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
  }

  .ligne-poubelle {
    margin-bottom: 15px;
  }

  label {
    display: block;
    font-weight: bold;
    margin-bottom: 6px;
    color: #2c3e50;
  }

  /* Les rectangles de saisie */
  input {
    width: 100%;
    padding: 10px;
    border: 2px solid #cfd8dc;
    border-radius: 6px;
    box-sizing: border-box;
    font-size: 15px;
  }

  input:focus {
    border-color: #4caf50;
    outline: none;
  }

  /* Tableau à droite */
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
  }

  th, td {
    border: 1px solid #e0e0e0;
    padding: 12px;
    text-align: left;
  }

  th {
    background-color: #2e7d32;
    color: white;
    border-radius: 4px 4px 0 0;
  }

  tr:nth-child(even) {
    background-color: #f9f9f9;
  }
  
  .badge-vaucluse {
    background-color: #e8f5e9;
    color: #2e7d32;
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 14px;
    font-weight: bold;
    display: inline-block;
  }
</style>

<h1 class="titre-site">🌿 ODD 12 - Cantine Éco-Responsable</h1>
<p style="text-align: center;">
  <span class="badge-vaucluse">Collège du Vaucluse — 700 Demi-pensionnaires</span>
</p>

<div class="ecran-partage">

  <div class="colonne-saisie">
    <h2 style="color: #2e7d32; margin-top: 0; border-bottom: 2px solid #e8f5e9; padding-bottom: 10px;">📋 Saisie des Pesées</h2>
    
    <div class="ligne-poubelle">
      <label>🥖 Poubelle à Pain</label>
      <input type="text" placeholder="Tapez le poids ici...">
    </div>

    <div class="ligne-poubelle">
      <label>🍎 Déchets Alimentaires (Assiettes)</label>
      <input type="text" placeholder="Tapez le poids ici...">
    </div>

    <div class="ligne-poubelle">
      <label>📦 Emballages</label>
      <input type="text" placeholder="Tapez le poids ici...">
    </div>

    <div class="ligne-poubelle">
      <label>🍏 Fruits Entamés</label>
      <input type="text" placeholder="Tapez le poids ici...">
    </div>

    <div class="ligne-poubelle">
      <label>🧻 Serviettes Papiers</label>
      <input type="text" placeholder="Tapez le poids ici...">
    </div>
  </div>

  <div class="colonne-affichage">
    <h2 style="color: #2e7d32; margin-top: 0; border-bottom: 2px solid #e8f5e9; padding-bottom: 10px;">📊 Tableau de Bord</h2>
    <p style="color: #666; font-size: 14px;">Les données actuelles de la cantine :</p>
    
    <table>
      <thead>
        <tr>
          <th>Catégorie de déchet</th>
          <th>Quantité enregistrée</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>🥖 Poubelle à Pain</strong></td>
          <td>À remplir à gauche</td>
        </tr>
        <tr>
          <td><strong>🍎 Déchets Alimentaires</strong></td>
          <td>À remplir à gauche</td>
        </tr>
        <tr>
          <td><strong>📦 Emballages</strong></td>
          <td>À remplir à gauche</td>
        </tr>
        <tr>
          <td><strong>🍏 Fruits Entamés</strong></td>
          <td>À remplir à gauche</td>
        </tr>
        <tr>
          <td><strong>🧻 Serviettes Papiers</strong></td>
          <td>À remplir à gauche</td>
        </tr>
      </tbody>
    </table>
  </div>

</div>
