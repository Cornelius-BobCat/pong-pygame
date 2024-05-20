# Pong Game

Ce projet est une implémentation simple du jeu classique Pong utilisant la bibliothèque Pygame en Python. Le jeu inclut un joueur humain contrôlant une raquette et un ordinateur contrôlant l'autre. L'objectif est de faire rebondir la balle pour marquer des points.

## Video Youtube 👇

[![vignette](https://i.ibb.co/F6Gd0Dw/Copie-de-RESEAU-3-D-REACT-NEXTJS-MONGO.png)](https://youtu.be/Iw6VcCu93PE)

## Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Exécution](#exécution)
- [Structure du Code](#structure-du-code)
- [Captures d'Écran](#captures-décran)
- [Contributions](#contributions)
- [Licence](#licence)

## Fonctionnalités

- Contrôle du paddle par le joueur à l'aide des flèches haut et bas du clavier.
- Contrôle de la raquette par l'ordinateur avec un algorithme simple.
- Affichage du score et de la vitesse de la balle.
- Enregistrement du meilleur score dans un fichier `best_score.txt`.
- Bouton de démarrage pour lancer le jeu.

## Prérequis

- Python 3.11
- Pygame

## Installation

1. Clonez ce dépôt sur votre machine locale :

   ```bash
   git clone https://github.com/Cornelius-BobCat/pong-pygame
   cd pong-pygame
   ```

2. Installez les dépendances :

   ```bash
   pip install pygame
   ```

## Exécution

Pour lancer le jeu, exécutez le script `main.py` :

```bash
python main.py
```

## Structure du Code

**Paddle** : Classe représentant une paddle.
**move_up()** : Déplace la paddle vers le haut.
**move_down()** : Déplace la raquepaddlette vers le bas.
**draw()** : Dessine la paddle sur l'écran.
**Ball** : Classe représentant la balle.

**move()** : Déplace la balle.
**display_speed()** : Affiche la vitesse actuelle de la balle.
**draw()** : Dessine la balle sur l'écran.

## Fonctions globales :

**save_score(score)** : Sauvegarde le meilleur score dans un fichier.
**best_score()** : Récupère le meilleur score du fichier.
**display_score()** : Affiche le score actuel et le meilleur score.
**play_button()** : Affiche le bouton "Play" pour démarrer le jeu.
**main()** : Fonction principale qui initialise le jeu et gère la boucle principale.

## Captures d'Écran

![pong](https://i.ibb.co/b10MjGC/Capture-d-cran-2024-05-21-00-25-30.png)

![pong](https://i.ibb.co/6sKgJKR/Capture-d-cran-2024-05-21-00-25-40.png)

## Contributions

Les contributions sont les bienvenues ! Veuillez soumettre une demande de PR (pull request) pour toute amélioration ou correction ✌️

## Licence

Ce projet est sous licence MIT.
