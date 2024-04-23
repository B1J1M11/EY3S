import numpy as np  # Numpy pour le traitement des tableaux multidimensionnels
import cv2          # OpenCV pour le traitement d'images et de vidéos
import os           # Os pour les opérations liées au système d'exploitation
import time         # Time pour manipuler le temps

# Chargement du classificateur en cascade pour la détection des visages
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Chemin du dossier pour enregistrer la capture d'écran
dossier_capture = "face"

# Si le dossier s'il n'existe pas déjà
if not os.path.exists(dossier_capture): 

    # crée le dossier
    os.makedirs(dossier_capture)    

cap = cv2.VideoCapture(0)   # Ouverture de la webcam
cap.set(3, 640)             # Définition de la largeur de la vidéo à 640 pixels
cap.set(4, 480)             # Définition de la hauteur de la vidéo à 480 pixels

# Variable pour suivre le temps de la dernière capture
derniere_capture = time.time()

# Variable pour suivre le nombre de visages capturés
num_visages_capture = 0

# Boucle principale pour capturer et traiter les images
while True:

    # Capture d'une image depuis la webcam
    ret, img = cap.read() 

    # Si l'image est Ewan Good
    if not ret:

        # Affiche une erreur dans la console
        print("Erreur lors de la lecture de l'image de la caméra.")

        # Sort du while
        break

    # Conversion de l'image en niveaux de gris
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Détection des visages dans l'image en niveaux de gris
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,     # Facteur de réduction de la taille de l'image
        minNeighbors=5,      # Nombre de voisins requis pour chaque candidat de rectangle
        minSize=(20, 20)     # Taille minimale du rectangle
    )

    # Boucle sur chaque visage détecté
    for (x, y, w, h) in faces:

        # Dessine un rectangle autour du visage
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Créer une fenetre focus sur le visage qui va être screen
        roi_color = img[y:y+h, x:x+w]

        # Affiche le visage en couleur
        cv2.imshow('Visage en couleur', roi_color)

        # Si le visage est bien identifié et clair
        if w * h > 10000:

            # Vérifie si 2 secondes se sont écoulées depuis la dernière capture
            temps_actuel = time.time()
            if temps_actuel - derniere_capture >= 2:
                
                # Enregistre l'image du visage en couleur dans le dossier spécifié
                chemin_capture = os.path.join(dossier_capture, f'visage_capture_{num_visages_capture}.png')

                # Enregistrement de l'image du visage capturé
                cv2.imwrite(chemin_capture, roi_color)

                # Affiche que l'image à été enregistrée dans la gallerie
                print(f"Capture du visage enregistrée dans le dossier 'face' sous le nom '{os.path.basename(chemin_capture)}'.")

                # Incrémente le compteur de visages capturés
                num_visages_capture += 1

                # Met à jour le temps de la dernière capture
                derniere_capture = temps_actuel

    # Affiche la vidéo avec les visages détectés
    cv2.imshow('Video', img)

    # Attendre la pression d'une touche (ESC) pour quitter
    k = cv2.waitKey(30) & 0xff

    # Si la touche appuyée est 'ESC'
    if k == 27:

        # Sortie de la boucle while et stop le programme
        break

cap.release()  # Libération de la ressource de capture vidéo
cv2.destroyAllWindows()  # Fermeture de toutes les fenêtres OpenCV
