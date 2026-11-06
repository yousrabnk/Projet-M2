# Simulateur de crédit

Application Streamlit qui indique combien on peut emprunter selon son salaire et la durée du prêt, puis qui détaille le coût du crédit : mensualité, intérêts, assurance et graphiques.

## Fonctionnalités
- montant maximal empruntable, avec une mensualité limitée à 30% du salaire
- message d'erreur si le prêt est impossible (mensualité supérieure à 30% du salaire)
- mensualité, coût total du crédit (somme des intérêts), assurance et montant total à rembourser
- graphiques des intérêts au cours du temps (par mois et cumulés)
- taux de la banque et taux d'assurance réglables dans la sidebar

## Installation

conda env create -f environment.yaml

conda activate streamlit

Paquets Python nécessaires : streamlit et pandas.

## Lancement

streamlit run projet.py

## Utilisation
1. Saisir le salaire mensuel et choisir la durée du prêt (5 à 25 ans) : le montant maximal empruntable s'affiche par la suite.
2. Saisir le montant du crédit : l'application indique si le prêt est possible ou non.
3. Consulter le détail des coûts et les graphiques pour mieux visualiser.
4. Modifier si besoin les taux de la banque dans la sidebar.

Les taux par défaut sont les suivants : 3,0 % (5 à 10 ans), 3,2 % (11 à 15 ans) et 3,5 % (16 à 25 ans). Le taux d'assurance est à 0 au lancement de l'application.

## Fonctionnement du code
Le code se trouve dans 'projet.py' :
- 'choisir_taux' : choisit le taux selon la durée (courte, moyenne, longue)
- 'calcul_mensualite' : calcule la mensualité
- 'credit_max' : retrouve le capital maximal à partir de la condition 30% du salaire 
- 'interets_par_mois' : calcule les intérêts de chaque mois pour les graphiques

## Limites 
- les taux par défaut sont des valeurs indicatives, pas de vrais taux de banque
- l'assurance n'est pas comptée dans les 30%