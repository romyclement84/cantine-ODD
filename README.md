<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Gestion des Déchets Cantine</title>
</head>
<body bgcolor="#F0F4F8" text="#2C3E50" link="#2E7D32">

  <center>
    <h1 style="color: #1B5E20; font-family: sans-serif;">🌿 ODD 12 - Cantine Éco-Responsable</h1>
    <p style="font-family: sans-serif; background-color: #E8F5E9; color: #2E7D32; padding: 5px; display: inline-block; border-radius: 10px;">
      <b>Collège du Vaucluse — 700 Demi-pensionnaires</b>
    </p>
  </center>

  <br>

  <table width="100%" border="0" cellspacing="20" cellpadding="0" style="font-family: sans-serif;">
    <tr>
      
      <td width="45%" valign="top" bgcolor="#FFFFFF" style="padding: 20px; border-radius: 12px; border: 1px solid #CFD8DC;">
        
        <h2 style="color: #2E7D32; margin-top: 0; border-bottom: 2px solid #E8F5E9; padding-bottom: 10px;">📋 Saisie des Pesées</h2>
        <p style="font-size: 14px; color: #666;">Indiquez le poids constaté (en kg ou grammes) :</p>
        
        <br>

        <p><b>🥖 Poubelle à Pain :</b></p>
        <input type="text" size="30" style="padding: 8px; border: 2px solid #CFD8DC; border-radius: 4px; width: 90%;" placeholder="Ex: 5 kg">

        <p><b>🍎 Déchets Alimentaires :</b></p>
        <input type="text" size="30" style="padding: 8px; border: 2px solid #CFD8DC; border-radius: 4px; width: 90%;" placeholder="Ex: 18.5 kg">

        <p><b>📦 Emballages :</b></p>
        <input type="text" size="30" style="padding: 8px; border: 2px solid #CFD8DC; border-radius: 4px; width: 90%;" placeholder="Ex: 2 kg">

        <p><b>🍏 Fruits Entamés :</b></p>
        <input type="text" size="30" style="padding: 8px; border: 2px solid #CFD8DC; border-radius: 4px; width: 90%;" placeholder="Ex: 1.2 kg">

        <p><b>🧻 Serviettes Papiers :</b></p>
        <input type="text" size="30" style="padding: 8px; border: 2px solid #CFD8DC; border-radius: 4px; width: 90%;" placeholder="Ex: 400 g">

        <br><br>
        <input type="button" value="Enregistrer les données" style="background-color: #2E7D32; color: white; padding: 12px; border: none; border-radius: 6px; width: 90%; font-weight: bold; cursor: pointer;">

      </td>

      <td width="55%" valign="top" bgcolor="#FFFFFF" style="padding: 20px; border-radius: 12px; border: 1px solid #CFD8DC;">
        
        <h2 style="color: #2E7D32; margin-top: 0; border-bottom: 2px solid #E8F5E9; padding-bottom: 10px;">📊 Tableau de Bord</h2>
        <p style="font-size: 14px; color: #666;">Toutes les données globales de l'établissement seront listées ici :</p>
        
        <br>

        <table width="100%" border="1" cellpadding="12" cellspacing="0" bordercolor="#E0E0E0" style="border-collapse: collapse;">
          <tr bgcolor="#2E7D32">
            <th><font color="white">Catégorie de déchet</font></th>
            <th><font color="white">Quantité mesurée</font></th>
          </tr>
          <tr>
            <td><b>🥖 Poubelle à Pain</b></td>
            <td><em>En attente de saisie...</em></td>
          </tr>
          <tr bgcolor="#F9F9F9">
            <td><b>🍎 Déchets Alimentaires</b></td>
            <td><em>En attente de saisie...</em></td>
          </tr>
          <tr>
            <td><b>📦 Emballages</b></td>
            <td><em>En attente de saisie...</em></td>
          </tr>
          <tr bgcolor="#F9F9F9">
            <td><b>🍏 Fruits Entamés</b></td>
            <td><em>En attente de saisie...</em></td>
          </tr>
          <tr>
            <td><b>🧻 Serviettes Papiers</b></td>
            <td><em>En attente de saisie...</em></td>
          </tr>
        </table>

      </td>

    </tr>
  </table>

</body>
</html>
