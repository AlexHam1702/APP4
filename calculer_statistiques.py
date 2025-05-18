def calculer_statistiques(villes_traitees):
    distances = [v['distance'] for v in villes_traitees]
    distances.sort()
    n = len(distances)
    return {
        'min': distances[0],
        'q1': distances[n // 4],
        'mediane': distances[n // 2],
        'max': distances[-1]
