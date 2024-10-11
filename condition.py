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