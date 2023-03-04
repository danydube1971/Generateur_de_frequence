"""Voici un script Python 3 pour Linux Mint qui génère une fréquence définie par l'utilisateur au format .WAV d'une durée de 5 secondes. 
Les fréquences supportées vont de 10 hertz à 20 kilohertz."""

import math
import struct
import wave

# Demander à l'utilisateur la fréquence souhaitée
freq = float(input("Entrez la fréquence désirée (10 - 20000 Hz): "))

# Vérifier que la fréquence est dans la plage de 10 à 20000 Hz
if freq < 10 or freq > 20000:
    print("Erreur: la fréquence doit être comprise entre 10 et 20000 Hz.")
    exit()

# Configurer les paramètres du fichier WAV
sample_width = 2  # Largeur d'échantillon en octets (2 = 16 bits)
num_channels = 1  # Nombre de canaux (1 = mono)
sample_rate = 44100  # Taux d'échantillonnage en Hz
num_frames = sample_rate * 5  # Nombre total de frames pour une durée de 5 secondes

# Créer un objet Wave_write et ouvrir un nouveau fichier WAV
wave_file = wave.open("freq.wav", "w")
wave_file.setparams((num_channels, sample_width, sample_rate, num_frames, "NONE", "not compressed"))

# Générer les échantillons pour la fréquence donnée
for i in range(num_frames):
    sample = int(32767.0 * math.sin(2 * math.pi * freq * i / sample_rate))
    packed_sample = struct.pack("<h", sample)
    wave_file.writeframes(packed_sample)

# Fermer le fichier WAV
wave_file.close()

print("Le fichier freq.wav a été créé avec succès.")

