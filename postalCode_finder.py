import csv 
import os.path

#with open("laposte_hexasmal.csv", "r") as fichier:
#    #on peut utiliser w pour write et a pour append
#    if os.path.exists("laposte_hexasmal.csv") == True:
#        print "le fichier existe"
#    else:
#        print "le fichier n'existe pas"
#    
#    file_Reader = csv.reader(fichier)
#    if file_Reader != None:
#        print "Jai reussi a charger le fichier"
#        
#    postal_codes = []
#    #copie chaque ligne dans la liste postal_codes
#    for row in file_Reader:
#        if len(row) != 0:
#            postal_codes.append(row)
#        else:
#            continue
        
with open("laposte_hexasmal.csv", "r") as fichier:
    #on peut utiliser w pour write et a pour append
    if os.path.exists("laposte_hexasmal.csv") == True:
        print "le fichier existe"
    else:
        print "le fichier n'existe pas"
    
    file_Reader = csv.DictReader(fichier, delimiter=';' )
    if file_Reader != None:
        print "Jai reussi a charger le fichier"
        
    communes = dict()
    #copie chaque ligne dans la liste postal_codes
    for row in file_Reader:
        if len(row) != 0:
            nom_commune = row['Nom_commune']
            code_postal = row['Code_postal']
            communes[code_postal] = nom_commune
        else:
            continue

def Commune(codePostal):
    if communes.has_key(str(codePostal)) == True:
        return communes[str(codePostal)]
    else:
        print "Ce code postal n'existe pas"

