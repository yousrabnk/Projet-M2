import streamlit as st

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


st.title("Simulateur de credit")

# reglages dans la sidebar pour les taux

st.sidebar.header("Reglages des taux de la banque")
taux_courte = st.sidebar.number_input("Taux pour 5 a 10 ans (%)", value=taux_courte, step=0.1)
taux_moyenne = st.sidebar.number_input("Taux pour 11 a 15 ans (%)", value=taux_moyenne, step=0.1)
taux_longue = st.sidebar.number_input("Taux pour 16 a 25 ans (%)", value=taux_longue, step=0.1)
taux_assurance = st.sidebar.number_input("Taux d'assurance (% du capital par an)", value=0.00, step=0.05)

# saisie de l'utilsateur

salaire = st.number_input("Salaire mensuel (euros)")
duree = st.slider("Duree du pret (annees)", 5, 25)

# affichage du montant maximal empruntable selon le salaire

taux=choisir_taux(duree)
maximum = credit_max(salaire, taux, duree)
st.info("Montant maximal empruntable selon votre salaire pour cette durée est de : " + str(round(maximum, 2)) + " euros, soit une mensualité maximale de : " + str(round(salaire * 0.3, 2)) + " euros")

# saisie du montant du credit

capital = st.number_input("Montant du credit (euros)")

# calculs

mensualite = calcul_mensualite(capital, taux, duree)
interet_total = mensualite * duree * 12 - capital
cout_total = mensualite * duree * 12
assurance_mensuelle = capital * taux_assurance / 100 / 12
cout_assurance = assurance_mensuelle * duree * 12

# affichage des resultats

st.subheader("Resultats pour un credit de " + str(capital) + " euros sur " + str(duree) + " ans :")

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

