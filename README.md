
# Simulateur de credit

Application streamlit : on rentre son salaire et le montant du credit demande, on choisit la duree avec un slider (5 a 25 ans) et le but est que l'appli affiche le montant maximal empruntable, la mensualite, le cout total du credit, la somme des interets et dise si le pret est possible (mensualite < 30% du salaire).

## Lancer
    streamlit run projet.py

## Ce qui est fait
- calcul de la mensualite et du cout total du credit (somme des interets)
- taux different selon la duree (courte / moyenne / longue) modifiables dans la sidebar
- montant maxiaml empruntable affiche des qe le salaire et la duree sont saisis
- message si le pret est impossible lorsque la mensualite depasse 30% du salaire
- saisie du salaire, du montant et de la duree 
- gestion d'un credit sans interet (taux = 0)

## Ce qui reste a faire
- graphique des interets
- ajouter le prix de l'assurnce

## Problemes 
- je n'ai pas de vrais taux de banque, j'ai mis des valeurs qui augmentent avec la duree
- je pense prendre pour le taux d'assurance par defaut (0,30%) mais il depend de l'age et du profil 

## Questions
- est ce qu'il faut mettre des valeur par défaut au lancement de l'application pour le salaire etc
- esrt ce que j'affiche tout de meme separement le montant total rembourse en plus de la somme des interets ? 