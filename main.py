import csv
import math
import time
import matplotlib.pyplot as plt
from lancer_programme import comparer_tris
from lancer_programme import lancerProgramme

if __name__ == "__main__":
    ville = input("Quelle ville voulez-vous rechercher ?")
    triChoisi = input("Quel tri voulez-vous utiliser ?")
    lancerProgramme(ville, "communes-france-2025.csv", type_tri=triChoisi)
    comparer_tris("communes-france-2025.csv")
