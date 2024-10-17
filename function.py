#fonction sans paramètre
def afficher_message():
    print("Hello World")

afficher_message()

#fonction avec paramètres
def afficher_message_nom(nom, prenom):
    print(f"Hello {nom} {prenom}")

afficher_message_nom("IRIMANANA", "Mahay")

#fonction avec valeur de retour
def somme(a, b):
    return a + b

result = somme(10, 20)
print(result)

#fonction calcul salaire mensuel à partir de salaire annuel
def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12

salaire_mensuel = salaire_mensuel(36000000)
print(f"Salaire mensuel : {salaire_mensuel}") 

#fonction calcul salaire hebdomadaire à partir de salaire mensuel
def salaire_hebdo(salaire_mensuel):
    return salaire_mensuel / 4

salaire_hebdo = salaire_hebdo(3000000)
print(f"Salaire hebdomadaire : {salaire_hebdo}")

#fonction calcul salaire horaire à partir de salaire hebdomadaire et heure de travail
def salaire_horaire(salaire_hebdo, heure_travail):
    return salaire_hebdo / heure_travail

salaire_horaire = salaire_horaire(3000000, 40)
print(f"Salaire horaire : {salaire_horaire}")