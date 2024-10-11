algo_password = False
email_type = 'admin'

def check_password(algo_password):
    if algo_password == True:
        print("Vous êtes connecté")
    elif email_type == 'admin':
        print("Vous etes connecté en tant qu'admin") 
    else:
        print("Mot de passe incorrect")


check_password(algo_password)

fruit = "pomme"

def check_fruit(fruit):
    match fruit:
        case "pomme":
            print("Pomme")
        case "cerise":
            print("Cerise")
        case "orange":
            print("Orange")
        case _:
            print("Je ne le connais pas")


check_fruit(fruit)