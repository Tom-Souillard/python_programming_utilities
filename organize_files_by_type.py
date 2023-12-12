"""
Usage:
Exécutez ce script dans un répertoire pour organiser automatiquement les fichiers dans des sous-dossiers appropriés selon leur type.

"""

import os
import shutil

# Définition des catégories de fichiers et leurs extensions correspondantes
CATEGORIES = {
    "Documents": ['.pdf', '.docx', '.txt'],
    "Images": ['.jpg', '.jpeg', '.png', '.gif'],
    "Videos": ['.mp4', '.mov', '.avi'],
    "Musiques": ['.mp3', '.wav', '.aac'],
    # Ajoutez ici d'autres catégories et extensions si nécessaire
}

def organize_files_by_type():
    """
    Organise les fichiers dans des sous-dossiers basés sur le type de fichier.
    """
    for fichier in os.listdir('.'):
        if os.path.isfile(fichier):
            extension_fichier = os.path.splitext(fichier)[1].lower()
            dossier_cible = None

            for categorie, extensions in CATEGORIES.items():
                if extension_fichier in extensions:
                    dossier_cible = categorie
                    break

            if dossier_cible:
                if not os.path.exists(categorie):
                    os.mkdir(categorie)
                shutil.move(fichier, os.path.join(dossier_cible, fichier))

def main():
    organize_files_by_type()
    print("Les fichiers ont été organisés dans des sous-dossiers.")

if __name__ == "__main__":
    main()
