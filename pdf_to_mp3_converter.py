"""
Usage:
Exécutez ce script dans un répertoire contenant des fichiers PDF pour les convertir en fichier .mp3

Dépendance:
- pyttsx3: Utilisé pour la conversion de texte en parole.
- PyPDF2: Utilisé pour lire les fichiers PDF.

Pour installer les dépendances, exécutez:
pip install pyttsx3 PyPDF2
"""

# Vérification des dépendances
try:
    import os
    import pyttsx3
    from PyPDF2 import PdfReader
except ModuleNotFoundError as e:
    module_manquant = str(e).split("'")[1]
    print(f"Erreur : Le module nécessaire '{module_manquant}' n'est pas installé.")
    print("Veuillez exécuter 'pip install pyttsx3 PyPDF2' pour installer les dépendances nécessaires.")
    exit(1)

def convert_pdf_to_mp3(chemin_pdf):
    """
    Convertit un fichier PDF en texte et le sauvegarde en tant que fichier audio MP3.

    Args:
        chemin_pdf (str): Chemin vers le fichier PDF à convertir.

    Returns:
        str: Texte complet extrait du fichier PDF.
    """
    lecteur_pdf = PdfReader(chemin_pdf)
    texte_complet = ""

    for page in lecteur_pdf.pages:
        texte = page.extract_text()
        if texte:
            texte_propre = texte.strip().replace('\n', ' ')
            texte_complet += texte_propre + " "

    return texte_complet

def main():
    synthetiseur_vocal = pyttsx3.init()
    fichiers_pdf = [f for f in os.listdir('.') if f.endswith('.pdf')]

    for fichier_pdf in fichiers_pdf:
        texte_complet = convert_pdf_to_mp3(fichier_pdf)
        fichier_mp3 = fichier_pdf.replace('.pdf', '.mp3')
        synthetiseur_vocal.save_to_file(texte_complet, fichier_mp3)

    synthetiseur_vocal.runAndWait()

if __name__ == "__main__":
    main()