# --- Stage 1 : Builder ---
FROM ubuntu:20.04 AS builder

# Pour éviter les prompts interactifs pendant l'installation
ARG DEBIAN_FRONTEND=noninteractive

# Mise à jour et installation de Python 3.9 et des outils de compilation
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    python3.9 \
    python3.9-dev \
    python3.9-venv \
    python3-pip \
    build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Création d'un environnement virtuel dans un chemin fixe
RUN python3.9 -m venv /home/fizzbuzz/venv
ENV PATH="/home/fizzbuzz/venv/bin:$PATH"

# Copier le fichier de dépendances et installer les packages
COPY requirement.txt .
RUN pip install --no-cache-dir wheel && \
    pip install --no-cache-dir -r requirement.txt

# --- Stage 2 : Runner ---
FROM ubuntu:20.04 AS runner

# Installation de Python 3.9 sur l'image finale
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    python3.9 \
    python3-venv && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Création d'un utilisateur non-root pour exécuter l'application
RUN useradd --create-home fizzbuzz

# Copier l'environnement virtuel construit dans le stage précédent
COPY --from=builder /home/fizzbuzz/venv /home/fizzbuzz/venv

# Passage à l'utilisateur non-root et préparation du répertoire de l'application
USER fizzbuzz
RUN mkdir /home/fizzbuzz/app
WORKDIR /home/fizzbuzz/app

# Copier tout le code de l'application dans le conteneur
COPY . .

# Assurer que les logs et messages s'affichent directement dans la console
ENV PYTHONUNBUFFERED=1

# Configuration de l'environnement virtuel
ENV VIRTUAL_ENV=/home/fizzbuzz/venv
ENV PATH="/home/fizzbuzz/venv/bin:$PATH"

# Commande de lancement de l'application (ici on lance le script main.py)
CMD ["python", "main.py"]
