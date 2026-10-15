import streamlit as st

# taux du credit selon la duree (en %)

taux_courte = 3.0    # 5 a 10 ans
taux_moyenne = 3.2   # 11 a 15 ans
taux_longue = 3.5    # 16 a 25 ans

def choisir_taux(duree):
    # choisit le taux selon la duree du pret
    if duree <= 10:
        return taux_courte
    elif duree <= 15:
        return taux_moyenne
    else:
        return taux_longue


def calcul_mensualite(capital, taux, duree):
    n = duree * 12          # nombre de mois
    i = taux / 100 / 12     # taux par mois
    mensualite = capital * i / (1 - (1 + i) ** (-n))
    return mensualite

# peut être faire une boucle si i = 0 pour evitr la division par 0

st.title("Simulateur de credit")

# saisie de l'utilsatuer
salaire = st.number_input("Salaire mensuel (euros)")
capital = st.number_input("Montant du credit (euros)")
duree = st.slider("Duree du pret (annees)", 5, 25)

# calculs
taux = choisir_taux(duree)
mensualite = calcul_mensualite(capital, taux, duree)
