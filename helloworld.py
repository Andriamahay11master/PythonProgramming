nom = "Mahay"
age = 32
nombre_flottante = 3.14
plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]
plateformes_sociales_supp = ["Whatsapp", "Youtube", "Twitch"]

def hello():
    if nom == "Mahay":
        print(f"Hello, Mahay, tu as {age} ans")
    else:
        print("Hello, World")

hello()

print("en sens normal",plateformes_sociales[0])
print("en sens inverse",plateformes_sociales[-3])
print("en sens normal",plateformes_sociales[0:2])
print("chaine considéré comme un tableau de lettres",plateformes_sociales[0][0])

# ajoute un nouveau element
plateformes_sociales.append("TikTok")
print(plateformes_sociales)

# supprime un element
plateformes_sociales.remove("Snapchat")
print(plateformes_sociales)

# pour calculer la longeur
taille_liste = len(plateformes_sociales)
print(taille_liste)

# pour trier la liste de maniere ascendant
plateformes_sociales.sort()
# pour trier la liste de maniere descendant
plateformes_sociales.sort( reverse=True )
print(plateformes_sociales)

# pour fusionner deux listes
plateformes_sociales.extend(plateformes_sociales_supp)
print(plateformes_sociales)

# pour ajouter un element dans la liste a une position specifique
plateformes_sociales.insert(1, "Snapchat")
print(plateformes_sociales)

# pour supprimer le dernier element et ajouter l'indice si on supprime un element 
plateformes_sociales.pop()
print(plateformes_sociales)

# pour trouver l'indice
plateformes_sociales.index("Snapchat")
print(plateformes_sociales.index("Snapchat"))

plateformes_sociales.append("Snapchat")
print(plateformes_sociales.count("Snapchat"))

# pour inverser une liste, identique à sort(reverse=True)
plateformes_sociales.reverse()
print(plateformes_sociales)

# pour vider une liste
plateformes_sociales.clear()
print(plateformes_sociales)