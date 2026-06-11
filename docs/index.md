


<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr>
<td rowspan="2"><img src="images/Image0.jpg"
style="width:1.38681in;height:1.47153in"
alt="logo_IGN_pour_lettre" /></td>
<td style="font-size: 24px;text-align: center;"><p><strong>Manuel utilisateur du plugin
« Altibonne »</strong></p>
<p><strong>V0.3.1</strong></p></td>
</tr>
<tr>
<td style="font-size: 16px;text-align: center;">Développeur  : Gérôme PECHEUR (IGN)</td>
</tr>
</tbody>
</table>


## Sommaire


- [1. Prérequis](#prerequis)
- [2. Résumé](#resume)
- [3. Installation](#installation)
- [4. Présentation](#presentation)
- [5. Utilisation](#5utilisation)
  - [5.1 Modification des Z d'un linéaire entier](#modification-des-z-dun-lineaire-entier)
  - [5.2 Modification du Z d'un point](#modification-du-z-dun-point)
  - [5.3 Navigation](#navigation) 



  
<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="prerequis" style="color: white;margin:0;" >1. Prérequis</h2>
</div>

Version de QGIS 3 : 3.28 ou supérieure.  
Ce plugin fonctionne en parallèle du plugin « IGN Espace collaboratif » version 4.2.2 et IGN_Maitre  



<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="resume" style="color: white;margin:0;" >2. Résumé</h2>
</div>

Ce plugin permet : 
-	De visualiser un profil sur des entités linéaires.  
-	De « relever/abaisser » tous les z d’un linéaire.  
-	De modifier ponctuellement un z sur un linéaire.  

  
  
<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="installation" style="color: white;margin:0;" >3. Installation</h2>
</div> 

Ouvrir QGIS.  
Allez dans **Extensions/Installer/Gérer les extensions**, cliquez sur **Installer depuis un ZIP**, sélectionner le fichier ZIP puis cliquez sur **Installer le plugin**.  

<div  style="text-align: center;"> 
	<img  src="images/Image1.png" /> 
</div>  
  
<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="presentation" style="color: white;margin:0;" >4. Présentation</h2>
</div>  
  

<div  style="text-align: center;"> 
	<img  src="images/Image2.jpg" /> 
</div>  

1.	Zone d‘affichage du profil  
2.	Valeur de delta Z permettant de relever ou d’abaisser tous les Z du linéaire sélectionné.  
3.	Valeur du Z correspondant au point sélectionné sur le linéaire.  
4.	Valeur du Z interpolé du point sélectionné correspondant à l'interpolation avec le Z du point avant et après sur le linéaire. Cette valeur peut être modifiée.  
5.	Valide la modification du linéaire en prenant en compte le delta Z renseigné.  
6.	Valide la modification du Z du point sélectionné en prenant en compte le Z interpolé ou tout autre Z renseigné par l’utilisateur.  
7.	Seuil de détection de pente, les segments du profil qui sont hors du seuil apparaissent en rouge.  
8.	Permet d’actualiser la vue du profil après un changement du seuil de détection de pente.  
9.	Ouvre une fenêtre retraçant l’historique des versions, cette documentation y est également accessible.  



 <div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="utilisation" style="color: white;margin:0;" >5. Utilisation</h2>
</div>

<div  style="font-size: 10px;background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="modification-des-z-dun-lineaire-entier" style="color: white;margin:0;" >5.1 Modification des Z d'un linéaire entier</h2>
</div>

Après avoir renseigné un delta Z, le bouton ![Image3](images/Image3.png) modifie les z de tous les points constituant le ou les linéaires sélectionnés.  
Le delta Z doit être compris entre -100 et 100 (mètres)  


<div  style="font-size: 10px;background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="modification-du-z-dun-point" style="color: white;margin:0;" >5.2 Modification du Z d'un point</h2>
</div>

Il faut sélectionner un point du linéaire sur le profil (clic gauche).  
Sur l’interface, le Z actuel du point est renseigné.  
Le Z interpolé est également renseigné. L’utilisateur peut modifier cette valeur s’il souhaite donner un Z différent de celui proposé.  
Le bouton ![Image4](images/Image4.png) modifie le Z du point sélectionné.  
L’interface s’actualise afin d’afficher le nouveau profil.  

<div  style="font-size: 10px;background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="navigation" style="color: white;margin:0;" >5.3 Navigation</h2>
</div>

Il est possible de :  
1.	Agrandir/rétrécir l’interface --> le profil suit.  
2.	Se déplacer dans le profil avec un clic gauche + déplacement (en dehors d’un point)  
3.	Zoomer dans le profil avec la molette de la souris  


