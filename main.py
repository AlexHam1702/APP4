import csv
import math
import time
import matplotlib.pyplot as plt

if __name__ == "__main__":
    lancer_programme("Maisons-Alfort", "communes-france-2025.csv", type_tri="fusion")
    comparer_tris("communes-france-2025.csv")
