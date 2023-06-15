# Generateur_de_frequence

Voici un script Python 3 pour Linux Mint qui génère une fréquence définie par l'utilisateur au format .WAV d'une durée de 5 secondes. 
Les fréquences supportées vont de 10 hertz à 20 kilohertz.

***Comment utiliser le script***

Exécuter le script dans un terminal avec la commande: **python3 "Générateur_de_fréquence.py"**

Testé dans Linux Mint

Ce que fais le script de manière détaillé:

1. Les modules math, struct et wave sont importés pour effectuer des opérations mathématiques, manipuler des données binaires et gérer des fichiers audio WAV respectivement.
2. L'utilisateur est invité à entrer la fréquence désirée en Hz.
3. La valeur de fréquence est vérifiée pour s'assurer qu'elle est comprise entre 10 et 20000 Hz. Si la valeur est en dehors de cette plage, un message d'erreur est affiché et le script se termine avec la fonction exit().
4. Les paramètres du fichier WAV sont configurés : la largeur d'échantillon est fixée à 2 octets (16 bits), le nombre de canaux est défini à 1 (mono), le taux d'échantillonnage est de 44100 Hz et le nombre total de frames est calculé en multipliant le taux d'échantillonnage par 5 (pour une durée de 5 secondes).
5. Un objet Wave_write est créé en ouvrant un nouveau fichier WAV nommé "freq.wav". Les paramètres du fichier WAV sont définis à l'aide de la méthode setparams() avec les valeurs précédemment configurées.
6. Une boucle for est utilisée pour générer les échantillons audio pour la fréquence donnée. La boucle itère sur le nombre total de frames.
7. À chaque itération, un échantillon est calculé en utilisant la formule math.sin(2 * math.pi * freq * i / sample_rate). Cette formule génère une onde sinusoïdale à la fréquence spécifiée.
8. L'échantillon est converti en entier et mis à l'échelle dans la plage des valeurs possibles pour un échantillon audio de 16 bits (de -32768 à 32767).
9. L'échantillon est ensuite empaqueté dans un format binaire <h à l'aide de la fonction struct.pack(). Ce format indique que l'échantillon est un entier court signé (short) et doit être encodé en little-endian (<).
10. L'échantillon empaqueté est écrit dans le fichier WAV à l'aide de la méthode writeframes() de l'objet Wave_write.
11. Une fois que toutes les frames ont été écrites, le fichier WAV est fermé avec la méthode close() de l'objet Wave_write.
12. Un message de confirmation est affiché pour indiquer que le fichier "freq.wav" a été créé avec succès.

En résumé, ce script demande à l'utilisateur une fréquence, génère une onde sinusoïdale à cette fréquence et enregistre cette tonalité dans un fichier audio WAV.


