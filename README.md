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

## Installation

1) Cloner le dépôt
```bash
git clone git@github.com:B1J1M11/EY3S.git
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

## Utilisation rapide

### Détection simple de visage (sans alerte)
```bash
python3 ey3s.py
```

### Détection + alerte WhatsApp (message instantané)
```bash
python3 cam.py
```

### Détection + envoi de l’image du visage sur WhatsApp
```bash
python3 cam2.py
```

Les images sont enregistrées dans le dossier `face/`

## Configuration

### Numéros de téléphone (WhatsApp)

- Dans `cam.py`, remplacez le numéro dans l’appel:
  - `pywhatkit.sendwhatmsg_instantly("+33XXXXXXXXX", "Mouvement détecté!")`
- Dans `cam2.py`, remplacez la variable `num`:
  - `num = "+33XXXXXXXXX"`

### Paramètres de détection (dans les scripts)

- `scaleFactor=1.2`, `minNeighbors=5`, `minSize=(20, 20)` contrôlent la détection Haar
- Seuil de surface du visage: `w * h > 10000` (capturer seulement les visages suffisamment grands)
- Délai entre deux captures: `2` secondes

## Limitations actuelles

- Numéros de téléphone et paramètres codés en dur dans les scripts
- Envoi WhatsApp via navigateur (bloquant et sujet aux aléas du focus)
- Pas de mode « headless » ni de paramètres en ligne de commande

## Axe d'amélioration 

- Passer par des ESP32.
- Utiliser un autre moyen que Whatsapp (fuck gafam).
- Intégré une API de reconnaissance faciale pour OSINT les visages capturés

## Références

- Article: [Real-time Face Recognition: An End-to-end Project](https://towardsdatascience.com/real-time-face-recognition-an-end-to-end-project-b738bb0f7348)
- Vidéo: [Série OpenCV — Détection/Reconnaissance](https://www.youtube.com/watch?v=bK_k7eebGgc&list=PLgNJO2hghbmhHuhURAGbe6KWpiYZt0AMH&index=1)

