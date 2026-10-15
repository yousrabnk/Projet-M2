
# Simulateur de credit

Application streamlit : on rentre son salaire et le montant du credit, on choisit la duree avec un slider (5 a 25 ans) et le but est que l'appli affiche la mensualite, le cout total et dise si le pret est possible (mensualite < 30% du salaire).

## Lancer
    streamlit run projet.py

## Ce qui est fait
- calcul de la mensualite
- taux different selon la duree (courte / moyenne / longue)
- saisie du salaire, du montant et de la duree 

## Ce qui reste a faire
- afficher les resultats
- message si le pret est impossible
- graphique des interets
- taux modifiables dans la sidebar 

## Problemes 
- je n'ai pas de vrais taux de banque, j'ai mis des valeurs qui augmentent avec la duree

## Questions
- est-ce qu'il faut prendre en compte l'assurance et les frais (TAEG) car sinon on sous estime le montant du credit ou alorsc'est pas pertinent car ce serait des valeurs fictives  ?