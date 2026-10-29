
# Simulateur de credit

Application streamlit : on rentre son salaire et le montant du credit demande, on choisit la duree avec un slider (5 a 25 ans) et le but est que l'appli affiche le montant maximal empruntable, la mensualite, le cout total du credit, le cout de l'assurance, la somme des interets et dise si le pret est possible (mensualite < 30% du salaire).

## Lancer
    streamlit run projet.py

## Ce qui est fait
- calcul de la mensualite et du cout total du credit (somme des interets)
- taux different selon la duree (courte / moyenne / longue) modifiables dans la sidebar
- montant maximal empruntable affiche des que le salaire et la duree sont saisis
- message si le pret est impossible lorsque la mensualite depasse 30% du salaire
- saisie du salaire, du montant et de la duree 
- gestion d'un credit sans interet (taux = 0)
- assurance du credit : taux modifiable dans la sidebar 
- affichage du cout total du credit avec assurance (interets + assurance)
- affichage du montant total a rembourser (capital + interets + assurance)

## Ce qui reste a faire
- graphique des interets

## Problemes 
- je n'ai pas de vrais taux de banque, j'ai mis des valeurs qui augmentent avec la duree
- le taux d'assurance depend de la banque et du profil de l'emprunteur (age, sante...), donc je n'ai pas mis de valeur par defaut : il est a 0 au lancement et l'utilisateur le modifie dans les reglages de la banque

## Questions
- est ce qu'il faut mettre des valeur par défaut au lancement de l'application pour le salaire, le taux d'assurance etc ?
