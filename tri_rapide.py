def tri_rapide(tableau):
    if len(tableau) <= 1:
        return tableau
    pivot = tableau[0]['distance']
    plus_petit = [x for x in tableau[1:] if x['distance'] <= pivot]
    plus_grand = [x for x in tableau[1:] if x['distance'] > pivot]
    return tri_rapide(plus_petit) + [tableau[0]] + tri_rapide(plus_grand)
