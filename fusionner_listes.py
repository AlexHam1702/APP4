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
