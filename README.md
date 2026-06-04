<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Stop au Gaspillage Alimentaire</title>
</head>
<body>

    <h1>Stop au Gaspillage Alimentaire ! 🍏</h1>
    <h3>Projet ODD - Collège du Vaucluse (700 demi-pensionnaires)</h3>
    <p>Bienvenue sur notre application de suivi des déchets de la cantine.</p>

    <hr>

    <div style="float: left; width: 45%; background-color: #f2f2f2; padding: 15px; border-radius: 8px;">
        <h2 style="color: green; margin-top: 0;">📋 1. Saisie des données</h2>
        <p>Remplissez les rectangles ci-dessous :</p>
        
        <p><b>🥖 Poubelle à Pain :</b><br>
        <input type="text" placeholder="Poids en kg..."></p>

        <p><b>🍎 Déchets Alimentaires :</b><br>
        <input type="text" placeholder="Poids en kg..."></p>

        <p><b>📦 Emballages :</b><br>
        <input type="text" placeholder="Poids en kg..."></p>

        <p><b>🍏 Fruits Entamés :</b><br>
        <input type="text" placeholder="Poids en kg..."></p>

        <p><b>🧻 Serviettes Papiers :</b><br>
        <input type="text" placeholder="Poids en kg..."></p>
        
        <br>
        <input type="button" value="Enregistrer la pesée" style="padding: 8px; background-color: green; color: white; border: none; font-weight: bold; cursor: pointer;">
    </div>

    <div style="float: right; width: 45%; background-color: #e8f5e9; padding: 15px; border-radius: 8px;">
        <h2 style="color: green; margin-top: 0;">📊 2. Données marquées</h2>
        <p>Voici les chiffres enregistrés pour l'établissement :</p>
        
        <table border="1" width="100%" cellpadding="8" style="background-color: white; border-collapse: collapse;">
            <tr style="background-color: green; color: white;">
                <th>Catégorie</th>
                <th>Poids</th>
            </tr>
            <tr>
                <td><b>🥖 Poubelle à Pain</b></td>
                <td>---</td>
            </tr>
            <tr>
                <td><b>🍎 Déchets Alimentaires</b></td>
                <td>---</td>
            </tr>
            <tr>
                <td><b>📦 Emballages</b></td>
                <td>---</td>
            </tr>
            <tr>
                <td><b>🍏 Fruits Entamés</b></td>
                <td>---</td>
            </tr>
            <tr>
                <td><b>🧻 Serviettes Papiers</b></td>
                <td>---</td>
            </tr>
        </table>
    </div>

    <div style="clear: both;"></div>

</body>
</html>
