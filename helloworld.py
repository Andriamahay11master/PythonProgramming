nom = "Mahay"
age = 32
nombre_flottante = 3.14
plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]

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

plateformes_sociales.append("TikTok")
print(plateformes_sociales)

plateformes_sociales.remove("Snapchat")
print(plateformes_sociales)

taille_liste = len(plateformes_sociales)
print(taille_liste)

plateformes_sociales.sort()
plateformes_sociales.sort( reverse=True )
print(plateformes_sociales)
