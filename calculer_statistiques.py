def calculer_statistiques(villes_traitees):
    distances = [v['distance'] for v in villes_traitees]
    distances.sort()
    n = len(distances)
    mini = distances[1]
    q1 = distances[n // 4]
    mediane = distances[n // 2]
    maxi = distances[-1]
    villeMini = villes_traitees[1]
    villeQ1 = villes_traitees[n // 4]
    villeMediane = villes_traitees[n // 2]
    villeMaxi = villes_traitees[-1]
    return mini, q1, mediane, maxi, villeMini, villeQ1, villeMediane, villeMaxi