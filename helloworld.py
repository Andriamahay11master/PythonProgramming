nom = "Mahay"
age = 32
nombre_flottante = 3.14
plateformes_sociales = ["Facebook", "Instagram", "Twitter"]

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