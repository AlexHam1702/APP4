import csv
import math
import time
import matplotlib.pyplot as plt

# Fonction pour lire les données du fichier CSV
def lire_donnees(fichier):
    liste_villes = []
    with open(fichier, 'r', encoding='utf-8') as fichier_csv:
        lecteur = csv.DictReader(fichier_csv, delimiter=',')
        for ligne in lecteur:
            try:
                nom = ligne['nom']
                latitude = float(ligne['latitude'])
                longitude = float(ligne['longitude'])
                liste_villes.append({'nom': nom, 'latitude': latitude, 'longitude': longitude})
            except:
                continue  # On ignore les lignes avec des données manquantes
    return liste_villes

# Fonction pour calculer la distance entre deux points avec la formule de Haversine
def calculer_distance(lat1, lon1, lat2, lon2):
    rayon_terre = 6371  # en kilomètres
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return rayon_terre * c

# Tri fusion (version simplifiée)
def tri_fusion(tableau):
    if len(tableau) <= 1:
        return tableau
    milieu = len(tableau) // 2
    gauche = tri_fusion(tableau[:milieu])
    droite = tri_fusion(tableau[milieu:])
    return fusionner_listes(gauche, droite)

def fusionner_listes(gauche, droite):
    resultat = []
    i = j = 0
    while i < len(gauche) and j < len(droite):
        if gauche[i]['distance'] < droite[j]['distance']:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
    resultat += gauche[i:]
    resultat += droite[j:]
    return resultat

# Tri rapide (version simple avec pivot)
def tri_rapide(tableau):
    if len(tableau) <= 1:
        return tableau
    pivot = tableau[0]['distance']
    plus_petit = [x for x in tableau[1:] if x['distance'] <= pivot]
    plus_grand = [x for x in tableau[1:] if x['distance'] > pivot]
    return tri_rapide(plus_petit) + [tableau[0]] + tri_rapide(plus_grand)

# Calcul des statistiques : min, 1er quartile, médiane, max
def calculer_statistiques(villes_traitees):
    distances = [v['distance'] for v in villes_traitees]
    distances.sort()
    n = len(distances)
    return {
        'min': distances[0],
        'q1': distances[n // 4],
        'mediane': distances[n // 2],
        'max': distances[-1]
    }

# Fonction principale pour tout faire (charger, calculer, trier, afficher)
def lancer_programme(nom_ville_reference, fichier_csv, type_tri="fusion"):
    villes = lire_donnees(fichier_csv)
    ville_ref = None
    for v in villes:
        if v['nom'].lower() == nom_ville_reference.lower():
            ville_ref = v
            break

    if ville_ref is None:
        print("La ville de référence n'a pas été trouvée.")
        return

    # On calcule la distance de chaque ville par rapport à la ville de référence
    for v in villes:
        v['distance'] = calculer_distance(
            ville_ref['latitude'], ville_ref['longitude'],
            v['latitude'], v['longitude']
        )

    # On trie selon le type choisi
    debut = time.time()
    if type_tri == "fusion":
        resultat = tri_fusion(villes)
    else:
        resultat = tri_rapide(villes)
    fin = time.time()

    # Affichage des statistiques
    stats = calculer_statistiques(resultat)
    print(f"\n--- Statistiques depuis {nom_ville_reference} ---")
    print(f"Distance minimale : {stats['min']:.2f} km")
    print(f"Premier quartile : {stats['q1']:.2f} km")
    print(f"Médiane : {stats['mediane']:.2f} km")
    print(f"Distance maximale : {stats['max']:.2f} km")
    print(f"Tri utilisé : {type_tri} | Durée : {fin - debut:.4f} secondes")

# Comparaison du tri fusion et du tri rapide en fonction de la taille
def comparer_tris(fichier_csv):
    tailles = [100, 500, 1000, 2000]
    temps_fusion = []
    temps_rapide = []

    toutes_les_villes = lire_donnees(fichier_csv)
    ville_ref = toutes_les_villes[0]

    for taille in tailles:
        sous_ensemble = toutes_les_villes[:taille]
        for v in sous_ensemble:
            v['distance'] = calculer_distance(
                ville_ref['latitude'], ville_ref['longitude'],
                v['latitude'], v['longitude']
            )

        debut_fusion = time.time()
        tri_fusion(sous_ensemble.copy())
        temps_fusion.append(time.time() - debut_fusion)

        debut_rapide = time.time()
        tri_rapide(sous_ensemble.copy())
        temps_rapide.append(time.time() - debut_rapide)

    plt.plot(tailles, temps_fusion, label='Tri fusion', marker='o')
    plt.plot(tailles, temps_rapide, label='Tri rapide', marker='x')
    plt.xlabel("Taille de l'échantillon")
    plt.ylabel("Temps d'exécution (s)")
    plt.title("Comparaison des algorithmes de tri")
    plt.legend()
    plt.grid(True)
    plt.show()

# Lancement automatique
if __name__ == "__main__":
    lancer_programme("Paris 1er Arrondissement", "votre_fichier.csv", type_tri="fusion")
    comparer_tris("votre_fichier.csv")
