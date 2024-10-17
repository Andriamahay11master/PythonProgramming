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