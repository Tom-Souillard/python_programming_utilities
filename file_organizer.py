import os
import shutil

def organize_files(directory):
    # Types de fichiers à organiser
    file_types = {
        'images': ['.jpg', '.jpeg', '.png', '.gif'],
        'documents': ['.pdf', '.doc', '.docx', '.txt', '.md', '.odt'],
        'audio': ['.mp3', '.wav', '.ogg', '.flac'],
        'video': ['.mp4', '.mkv', '.flv', '.mpeg'],
        # Ajoutez d'autres types de fichiers si nécessaire
    }

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1]
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    folder_path = os.path.join(directory, folder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    break

# Utilisation
# organize_files('chemin/vers/le/dossier')
