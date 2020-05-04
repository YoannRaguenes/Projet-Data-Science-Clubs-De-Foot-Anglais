<!DOCTYPE HTML>

<html>

  <head>
    <title>Création de compte</title>
    <meta content="info">
    <meta charset="UTF-8">
    <link rel="stylesheet" href="gestion_batiment.css" />
  </head>
  
  <body id='fond'>
 <div>
 	<h1> Créer un compte </h1>
 	
<form method="POST">
	<fieldset>
 		<legend> Coordonnées </legend>

       <p>
       Veuillez indiquer si la personne est :<br />
       <input type="radio" name="role" value="etu" id="etu" /> <label for="etu">Etudiant</label><br />
       <input type="radio" name="role" value="enseignant" id="enseignant-25" /> <label for="enseignant-25">Enseignant</label><br />
       <input type="radio" name="role" value="service" id="service" /> <label for="service">Du service Technique</label><br />
       </p>

       <p><label for="nom">Nom :</label>
       <input type="text" name="nom" id="nom" /></p>

       <p><label for="prenom">Prénom :</label>
       <input type="text" name="prenom" id="prenom" /></p>

       <p><label for="classe">classe ou département :</label>
       <input type="text" name="classe" id="classe" /></p>


       <p><label for="email">Email :</label>
       <input type="email" name="email" id="email" /></p>
 
        
       <input type="submit" value="Valider" />
   </fieldset>
       </form>
<?php 
                    if(isset($erreur))
                    {
                        echo '<span style="color:red">'.$erreur.'</span>';
                    }
                    else 
                    {
                        echo'<br />';
                    }    
                ?>

</div>
  
  </body>
</html> 
