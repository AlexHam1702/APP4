import csv
import math
import time
import matplotlib.pyplot as plt


# Tri fusion
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

# Tri rapide
def tri_rapide(tableau):
    if len(tableau) <= 1:
        return tableau
    pivot = tableau[0]['distance']
    plus_petit = [x for x in tableau[1:] if x['distance'] <= pivot]
    plus_grand = [x for x in tableau[1:] if x['distance'] > pivot]
    return tri_rapide(plus_petit) + [tableau[0]] + tri_rapide(plus_grand)

# Calcul des statistiques
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

# Fonction principale
def lancer_programme(nom_ville_reference, fichier_csv, type_tri="fusion"):
    villes = lire_donnees(fichier_csv)
    if not villes:
        print("Aucune ville chargée. Vérifiez le fichier CSV.")
        return

    ville_ref = None
    for v in villes:
        if v['nom'].lower() == nom_ville_reference.lower():
            ville_ref = v
            break

    if ville_ref is None:
        print("La ville de référence n'a pas été trouvée.")
        return

    # Calcul de distance
    for v in villes:
        v['distance'] = calculer_distance(
            ville_ref['latitude'], ville_ref['longitude'],
            v['latitude'], v['longitude']
        )

    # Tri
    debut = time.time()
    if type_tri == "fusion":
        resultat = tri_fusion(villes)
    else:
        resultat = tri_rapide(villes)
    fin = time.time()

    # Statistiques
    stats = calculer_statistiques(resultat)
    print(f"\n--- Statistiques depuis {nom_ville_reference} ---")
    print(f"Distance minimale : {stats['min']:.2f} km")
    print(f"Premier quartile : {stats['q1']:.2f} km")
    print(f"Médiane : {stats['mediane']:.2f} km")
    print(f"Distance maximale : {stats['max']:.2f} km")
    print(f"Tri utilisé : {type_tri} | Durée : {fin - debut:.4f} secondes")

# Comparaison des tris
def comparer_tris(fichier_csv):
    tailles = [100, 500, 1000, 2000]
    temps_fusion = []
    temps_rapide = []

    toutes_les_villes = lire_donnees(fichier_csv)
    if not toutes_les_villes:
        print("Erreur : fichier CSV vide ou invalide.")
        return

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

# main 
if __name__ == "__main__":
    lancer_programme("Maisons-Alfort", "communes-france-2025.csv", type_tri="fusion")
    comparer_tris("communes-france-2025.csv")
