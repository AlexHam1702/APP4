import csv
def lire_donnees(fichier):
    liste_villes = []
    with open(fichier, 'r', encoding='utf-8') as fichier_csv:
        lecteur = csv.DictReader(fichier_csv, delimiter=',')
        for ligne in lecteur:
            try:
                nom = ligne['nom_sans_accent']
                latitude = float(ligne['latitude_mairie'])
                longitude = float(ligne['longitude_mairie'])
                liste_villes.append({'nom': nom, 'latitude': latitude, 'longitude': longitude})
            except:
                continue  # Ignore les lignes mal formées
    return liste_villes
