# FizzBuzz - Efrei

## Description

Ce projet implémente la fonction FizzBuzz avec des règles étendues. Pour un nombre `n`, la fonction :
- Ajoute "Fizz" si `n` est divisible par 3.
- Ajoute "Fizz" si `n` contient le chiffre 3.
- Ajoute "Buzz" si `n` est divisible par 5.
- Ajoute "Buzz" si `n` contient le chiffre 5.
- Si aucune de ces conditions n'est remplie, retourne `n` sous forme de chaîne.

Le projet inclut :
- Le code source de l'application (fichiers `fizzbuzz.py` et `main.py`)
- Des tests unitaires (dans `test_fizzbuzz.py`)
- Une configuration GitHub Actions pour l'exécution des tests et la génération d'un rapport de couverture
- Une configuration Docker pour containeriser l'application et déployer l'image sur DockerHub

## Prérequis

- **Git** : Pour cloner le dépôt et gérer les branches.
- **Python 3.9+** : Pour exécuter l'application et les tests.
- **Docker** : Pour construire l'image et exécuter l'application dans un container.
- **GitHub Actions** : Pour l'intégration continue (CI) et le déploiement.

## Installation et Exécution

### Installation locale

1. **Cloner le dépôt :**
    ```bash
    git clone https://github.com/Amiiircmoi/fizzbuzz-Efrei.git
    cd FizzBuzz-Efrei
    ```

2. **Créer et activer un environnement virtuel (optionnel) :**
    ```bash
    python3.9 -m venv venv
    source venv/bin/activate
    ```

3. **Installer les dépendances :**
    ```bash
    pip install --no-cache-dir -r requirement.txt
    ```

4. **Exécuter l'application :**
    ```bash
    python main.py
    ```

### Exécution des tests

Pour lancer les tests unitaires et générer un rapport de couverture, exécutez :
```bash
python -m unittest discover
coverage run -m unittest discover
coverage report
```

## Utilisation de Docker

### Construire l'image Docker

Le projet dispose d'un Dockerfile multi-stage pour construire une image légère.
```bash
docker build -t fizzbuzz-app .
```

### Exécuter l'application dans un container

Pour exécuter l'application dans un container Docker, exécutez la commande suivante :
```bash
docker run --rm fizzbuzz-app
```

### Lancer les tests dans un container

Pour exécuter les tests unitaires dans un container Docker, exécutez la commande suivante :
```bash
docker run --rm fizzbuzz-app python -m unittest discover
```

## Workflows GitHub Actions

Le dépôt contient deux workflows principaux :

1. **Tests Python**
  Le fichier `.github/workflows/python_test.yml` :
  - Se déclenche lors d'un push ou d'une pull request sur la branche `main`.
  - Configure l'environnement Python, installe les dépendances et exécute les tests unitaires avec `coverage`.
  - Génère et upload un rapport HTML de couverture.

2. **Docker Build & Deploy**
  Le fichier `.github/workflows/docker_deploy.yml` (déclenché manuellement via `workflow_dispatch`) :
  - Vérifie la présence d'un Dockerfile avant de continuer.
  - Configure Docker Buildx, se connecte à DockerHub et construit l'image Docker.
  - Pousse l'image sur DockerHub (assure-toi que les secrets sont configurés, voir ci-dessous).
  - Exécute ensuite les tests unitaires dans le container construit.

## Configuration des Secrets pour DockerHub

Pour déployer l'image Docker sur DockerHub via GitHub Actions, ajoutez les secrets suivants dans votre dépôt :
1. Accédez à **Settings > Secrets and variables > Actions**.
2. Cliquez sur **New repository secret** et ajoutez :
     - **DOCKERHUB_USERNAME** : Votre nom d'utilisateur DockerHub.
     - **DOCKERHUB_TOKEN** : Votre token d'accès DockerHub.

Ces secrets sont utilisés dans le workflow pour se connecter à DockerHub et pousser l'image.

## Processus de Contribution et Protection de la Branche `main`

### Protection de la branche main

Pour éviter les push directs, configurez une règle de protection sur la branche main dans **Settings > Branches**. Exigez :
  - Une revue de pull request avant merge.
  - Le succès des tests (status check) avant de pouvoir merger une pull request.

### Branches de fonctionnalités

Chaque nouvelle évolution doit être développée sur une branche dédiée (feature branch) et intégrée via une pull request vers `main`.

### Déclenchement Manuel des Workflows

Pour lancer manuellement le workflow Docker (par exemple, pour tester la construction et le déploiement de l'image) :
- Assurez-vous que le workflow est présent dans la branche par défaut ou utilisez l'API GitHub.
- Allez dans l'onglet Actions sur GitHub, sélectionnez le workflow "Docker Build and Deploy" et cliquez sur **Run workflow**.

## Contact

Pour toute question ou suggestion, veuillez contacter Amir ANCIAUX (amiiircmoi).
