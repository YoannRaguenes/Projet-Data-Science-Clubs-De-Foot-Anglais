 <?php
 include('connect_bdd.php');

    function passgen2($nbChar){
    return substr(str_shuffle(
'abcdefghijklmnopqrstuvwxyzABCEFGHIJKLMNOPQRSTUVWXYZ0123456789'),1, $nbChar); }
    if(isset($_POST['nom']) && isset($_POST['email']) && isset($_POST['mpd']) && isset($_POST['role'])){

    	$nom = $_POST['nom'];
      $prenom = $_POST['prenom'];
    	$email = $_POST['email'];
    	$mpd = passgen2(10);
    	
    	
    	// Hachage du mot de passe
$pass_hache = password_hash($mpd, PASSWORD_DEFAULT);

// Insertion
$req = $bdd->prepare("INSERT INTO personne (nom, prenom, email, password) VALUES (?,?,?,?)");
$req->execute(array( $nom, $prenom, $email, $pass_hache));

$sql ="SELECT `id_personne` FROM `personne` WHERE email='$email'";
$req =$bdd->prepare($sql);
$req->execute();
$result = $req-> fetchAll();
$id_personne = $result[0][0];

if($_POST['role']=='etu'){
$req = $bdd->prepare("INSERT INTO `etudiant`( `classe`,`id_perso`) VALUES (?,?)");
$req->execute(array($_POST['classe'],$id_personne));
}
elseif ($_POST['role']== 'enseignant') {

$req = $bdd->prepare("INSERT INTO `enseignant`(`departement`, `id_pers`) VALUES (?,?)");
$req->execute(array($_POST['classe'], $id_personne));
  
}
else{

$req = $bdd->prepare("INSERT INTO `service_technique`(`departement`, `id_person`) VALUES (?,?)");
$req->execute(array($_POST['classe'],$id_personne));

}

//Verification si l'email est deja dans la base de recuperation
$mail_recup_exist = $base->prepare('SELECT id_personne FROM personne WHERE email = ?');
$mail_recup_exist->execute(array($email));
$mail_recup_exist = $mail_recup_exist->rowCount();


$dest = $email;
$sujet = "Création de votre compte ";
$corps = "Bonjour, votre compte a été créer par l'administrateur, votre mot de passe est: " . $mpd;
$headers = "From: adriensimard05@gmail.com";

if($mail_recup_exist==1){
$erreur = "Adresse mail deja existante .";
}
else {
  mail($dest, $sujet, $corps, $headers);
  echo "Email envoyé avec succès";
} 

}
require_once('form_inscrip_view.php');


    ?>