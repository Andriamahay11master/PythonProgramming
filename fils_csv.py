import csv

#with reader
with open('couleurs_preferees.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row[0], row[1], row[2])

print('\n')
#with DictReader
with open('couleurs_preferees.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['nom'], row['metier'], row['couleur_preferee'])        