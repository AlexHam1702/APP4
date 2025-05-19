from lire_donnees import lire_donnees
from calculer_distance import calculer_distance
from tri_fusion import tri_fusion
import time as time
from calculer_statistiques import calculer_statistiques
from tri_rapide import tri_rapide
import matplotlib.pyplot as plt
def lancerProgramme(nom_ville_reference, fichier_csv, type_tri="fusion"):
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
    mini, q1, mediane, maxi, villeMini, villeQ1, villeMediane, villeMaxi = calculer_statistiques(resultat)
    print(f"Distance minimale : {mini:.2f} km : {villeMini['nom']}")
    print(f"Premier quartile : {q1:.2f} km: {villeQ1['nom']}")
    print(f"Médiane : {mediane:.2f} km: {villeMediane['nom']}")
    print(f"Distance maximale : {maxi:.2f} km: {villeMaxi['nom']}")
    print(f"Tri utilisé : {type_tri} | Durée  : {fin - debut:.4f} secondes")

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
