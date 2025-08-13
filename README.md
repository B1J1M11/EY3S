## EY3S

`EY3S` est un petit système de surveillance par webcam basé sur OpenCV. Il détecte les visages, capture des images et peut envoyer une alerte via WhatsApp Web.

### Fonctionnalités

- **Détection de visage en temps réel** avec des rectangles de surbrillance
- **Captures d’écran** des visages détectés (dossier `face/`)
- **Alertes WhatsApp Web** (message instantané ou envoi d’image) via `pywhatkit`
- Base pour une future **reconnaissance faciale** (à venir)

## Prérequis

- Python 3.8+
- Webcam fonctionnelle
- Navigateur par défaut installé et accessible (WhatsApp Web est utilisé par `pywhatkit`)
- Connexion Internet stable

## Installation

1) Cloner le dépôt
```bash
git clone <url-du-repo>
cd EY3S
```

2) (Optionnel mais recommandé) Créer un environnement virtuel
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3) Installer les dépendances
```bash
pip install --upgrade pip
pip install opencv-python numpy pywhatkit playsound
```

Le fichier de cascade Haar `haarcascade_frontalface_default.xml` est déjà fourni dans le dépôt. L’application attend ce fichier à la racine du projet.

## Utilisation rapide

### Détection simple de visage (sans alerte)
```bash
python3 ey3s.py
```

### Détection + alerte WhatsApp (message texte instantané)
```bash
python3 cam.py
```

### Détection + envoi de l’image du visage sur WhatsApp
```bash
python3 cam2.py
```

Les images sont enregistrées dans le dossier `face/` (créé automatiquement au premier lancement).

## Configuration

### Numéros de téléphone (WhatsApp)

- Dans `cam.py`, remplacez le numéro dans l’appel:
  - `pywhatkit.sendwhatmsg_instantly("+33XXXXXXXXX", "Mouvement détecté!")`
- Dans `cam2.py`, remplacez la variable `num`:
  - `num = "+33XXXXXXXXX"`

Assurez-vous d’utiliser l’indicatif pays (ex: `+33` pour la France) et que le numéro est associé à un compte WhatsApp actif.

### Paramètres de détection (dans les scripts)

- `scaleFactor=1.2`, `minNeighbors=5`, `minSize=(20, 20)` contrôlent la détection Haar
- Seuil de surface du visage: `w * h > 10000` (capturer seulement les visages suffisamment grands)
- Délai entre deux captures: `2` secondes

Ces valeurs peuvent être ajustées selon votre caméra et votre scène.

## Comment ça marche

1) Ouvre la webcam et lit des images en continu
2) Convertit en niveaux de gris puis détecte les visages via un classificateur Haar
3) Dessine des rectangles et (selon le script) capture/alerte via WhatsApp

## Conseils et dépannage

- Au premier envoi avec `pywhatkit`, votre navigateur s’ouvrira sur WhatsApp Web. Scannez le QR code si demandé.
- Évitez d’utiliser la souris/clavier pendant l’automatisation de `pywhatkit` (il contrôle le navigateur quelques secondes).
- Si la caméra ne s’ouvre pas, vérifiez qu’aucune autre application ne l’utilise et que `cv2.VideoCapture(0)` fonctionne.
- Si aucune détection n’apparaît, rapprochez-vous de la caméra ou baissez le seuil `w*h`.
- Le son (`playsound`) et l’envoi WhatsApp peuvent être bloquants; c’est normal dans ces scripts simples.

## Limitations actuelles

- Numéros de téléphone et paramètres codés en dur dans les scripts
- Envoi WhatsApp via navigateur (bloquant et sujet aux aléas du focus)
- Pas de mode « headless » ni de paramètres en ligne de commande

## Feuille de route (idées)

- Paramétrage via `argparse` ou fichier YAML/ENV
- Envoi d’alertes non bloquant (threading) et anti-spam/cooldown distinct
- Reconnaissance faciale (base locale, embeddings, etc.)
- Mode headless (sans `imshow`) pour serveur
- Journalisation via `logging` et meilleure gestion d’erreurs

## Avertissement légal

Respectez la législation en vigueur concernant la surveillance vidéo et la protection des données personnelles. Informez les personnes susceptibles d’être filmées et stockez les données de façon sécurisée.

## Références

- Article: [Real-time Face Recognition: An End-to-end Project](https://towardsdatascience.com/real-time-face-recognition-an-end-to-end-project-b738bb0f7348)
- Vidéo: [Série OpenCV — Détection/Reconnaissance](https://www.youtube.com/watch?v=bK_k7eebGgc&list=PLgNJO2hghbmhHuhURAGbe6KWpiYZt0AMH&index=1)

