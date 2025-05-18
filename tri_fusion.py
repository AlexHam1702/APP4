# Tri fusion
def tri_fusion(tableau):
    if len(tableau) <= 1:
        return tableau
    milieu = len(tableau) // 2
    gauche = tri_fusion(tableau[:milieu])
    droite = tri_fusion(tableau[milieu:])
    return fusionner_listes(gauche, droite)
