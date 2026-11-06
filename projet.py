import streamlit as st
import pandas as pd

# taux du credit selon la duree (en %)

taux_courte = 3.0    # 5 a 10 ans
taux_moyenne = 3.2   # 11 a 15 ans
taux_longue = 3.5    # 16 a 25 ans

# fonctions

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
    if i == 0: # sans interets
        mensualite = capital / n
    else:
        mensualite = capital * i / (1 - (1 + i) ** (-n))
    return mensualite

def credit_max(salaire,taux,duree):
    n = duree * 12          # nombre de mois
    i = taux / 100 / 12     # taux par mois
    mensualite_max = salaire * 0.3
    if i == 0: 
        capital_max = mensualite_max * n
    else:
        capital_max = mensualite_max * (1 - (1 + i) ** (-n)) / i
    return capital_max

def interets_par_mois(capital, taux, duree):
    # renvoie la liste des interets payes chaque mois
    mensualite = calcul_mensualite(capital, taux, duree)
    i = taux / 100 / 12    # taux par mois
    restant = capital
    liste_interets = []
    for mois in range(duree * 12):
        interet = restant * i   # interet du mois sur le capital restant
        liste_interets.append(interet)
        restant = restant - (mensualite - interet)  # capital restant apres paiement de la mensualite
    return liste_interets    

st.title("Simulateur de crédit")

# reglages dans la sidebar pour les taux

st.sidebar.header("Réglages des taux de la banque")
taux_courte = st.sidebar.number_input("Taux pour 5 à 10 ans (%)", value=taux_courte, min_value=0.0, step=0.1)
taux_moyenne = st.sidebar.number_input("Taux pour 11 à 15 ans (%)", value=taux_moyenne, min_value=0.0, step=0.1)
taux_longue = st.sidebar.number_input("Taux pour 16 à 25 ans (%)", value=taux_longue, min_value=0.0, step=0.1)
taux_assurance = st.sidebar.number_input("Taux d'assurance (% du capital par an)", value=0.00, min_value=0.0, step=0.1)

# saisie de l'utilsateur

salaire = st.number_input("Salaire mensuel (euros)", min_value=0.0)
duree = st.slider("Durée du prêt (années)", 5, 25)

# affichage du montant maximal empruntable selon le salaire

taux=choisir_taux(duree)
maximum = credit_max(salaire, taux, duree)
st.info("Montant maximal empruntable selon votre salaire pour cette durée est de : " + str(round(maximum, 2)) + " euros, soit une mensualité maximale de : " + str(round(salaire * 0.3, 2)) + " euros")

# saisie du montant du credit

capital = st.number_input("Montant du crédit (euros)", min_value=0.0)

# calculs

mensualite = calcul_mensualite(capital, taux, duree)
interet_total = mensualite * duree * 12 - capital
cout_total = mensualite * duree * 12
assurance_mensuelle = capital * taux_assurance / 100 / 12
cout_assurance = assurance_mensuelle * duree * 12

# affichage des resultats

st.subheader("Résultats pour un crédit de " + str(capital) + " euros sur " + str(duree) + " ans :")

# pret impossible si la mensulaite depasse 30% du salaire

if mensualite > salaire * 0.3:
    st.error("La mensualité de " + str(round(mensualite, 2)) + " euros dépasse 30% du salaire. Le prêt est impossible. Il faut soit diminuer le montant du crédit, soit augmenter la durée du prêt.")
else:
    st.success("Le prêt est possible.")    

st.write("Taux :", taux, "%")
st.write("Mensualité :", round(mensualite, 2), "euros")
st.write("Coût total du crédit (intérêts) :", round(interet_total, 2), "euros")
st.write("Assurance :", round(assurance_mensuelle, 2), "euros par mois")
st.write("Coût total de l'assurance :", round(cout_assurance, 2), "euros")
st.write("Coût total du crédit avec assurance (intérêts + assurance) :", round(interet_total + cout_assurance, 2), "euros")
st.write("Montant total à rembourser (capital + intérêts + assurance) :", round(cout_total + cout_assurance, 2), "euros")

# graphique des interets en fonction du temps

liste_interets = interets_par_mois(capital, taux, duree)
df = pd.DataFrame({"Mois": range(1, len(liste_interets) + 1),
                   "Intérêts du mois (euros)": liste_interets})
df["Intérêts cumulés (euros)"] = df["Intérêts du mois (euros)"].cumsum()

st.subheader("Graphique des intérêts au cours du temps")
st.write("Intérêts payés chaque mois :")
st.line_chart(df, x="Mois", y="Intérêts du mois (euros)")
st.write("Intérêts cumulés au cours du temps :")
st.line_chart(df, x="Mois", y="Intérêts cumulés (euros)")