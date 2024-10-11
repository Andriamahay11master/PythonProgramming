liste_marque_voiture = ["audi", "bmw", "mercedes", "renault", "volkswagen"]

def display_marque(liste):
    for marque in liste:
        print(marque)


display_marque(liste_marque_voiture)

def display_number(number):
    for x in range(number):
        print(x)    

display_number(10)

capacite_maximale = 10
capacite_actuelle = 3

while capacite_actuelle < capacite_maximale:
    capacite_actuelle += 1
    print(capacite_actuelle)

#exemple utilisation de break et continue

for x in range(10):
    if x == 5:
        break
    print("test break",x)        

for x in range(10):
    if x == 5:
        continue
    print("test continue",x)