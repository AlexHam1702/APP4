def calculer_statistiques(villes_traitees):
    distances = [v['distance'] for v in villes_traitees]
    distances.sort()
    n = len(distances)
    mini = distances[0]
    q1 = distances[n // 4]
    mediane = distances[n // 2]
    maxi = distances[-1]
    return mini, q1, mediane, maxi