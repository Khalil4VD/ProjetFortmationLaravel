#!/bin/bash

# Répertoire où vous souhaitez rechercher les fichiers .txt
directory="/chemin/vers/votre/répertoire"

# Recherche récursive des fichiers .txt dans le répertoire spécifié
files=$(find "$directory" -type f -name "*.txt")

# Création du répertoire txt_files dans le répertoire courant
mkdir -p ./txt_files

# Copie des fichiers trouvés dans le répertoire txt_files
for file in $files; do
    cp "$file" ./txt_files
done

# Nombre total de fichiers copiés
count=$(find ./txt_files -type f | wc -l)

# Affichage du nombre total de fichiers copiés
echo "Nombre total de fichiers copiés : $count"
