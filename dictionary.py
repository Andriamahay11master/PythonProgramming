#déclaration dictionary
new_campagne = {
    "nom" : "Campagne 2022",
    "date" : "1er Janvier 2022",
    "duree" : "3 semaines",
    "plateformes" : ["Facebook", "Instagram", "Snapchat", "Twitter"],
}
print(new_campagne)

#déclaration dictionnaire vide ou {}
new_campagne_rs = dict()
print(new_campagne_rs)

#déclaration dictionnaire avec clefs et values définies
new_campagne_rs['fb'] = "Facebook"
new_campagne_rs['ig'] = "Instagram"
print(new_campagne_rs)

#changement valeur de clef dictionnaire
new_campagne["date"] = "2er Janvier 2022"
new_campagne["plateformes"].append("TikTok")
print(new_campagne)

#suppression d'une clef dictionnaire
del new_campagne["duree"]
new_campagne['test'] = 23
new_campagne.pop("test")
print(new_campagne)