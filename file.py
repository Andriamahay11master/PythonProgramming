#write in file
fichier = open("file.txt", "w")
fichier.write("End of File")
fichier.close()

#add text in file
fichier = open("file.txt", "a")
fichier.write("\nEnd of File")
fichier.close()