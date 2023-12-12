"""
Usage:
Ce script envoie automatiquement des rappels de rendez-vous par e-mail ou SMS.
Il lit un fichier contenant les rendez-vous (date, heure, et information de contact) et envoie un rappel un jour avant chaque rendez-vous.

Dépendances:
- pandas: Pour lire le fichier de données.
- smtplib ou une API de messagerie tiers (comme Twilio pour SMS): Pour envoyer les e-mails ou SMS.

Installez les dépendances nécessaires avec:
pip install pandas twilio
"""

import pandas as pd
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration de l'email
email_address = "votre_adresse_email@example.com"
email_password = "votre_mot_de_passe"

# Lire les données des rendez-vous
def lire_rendez_vous(fichier):
    return pd.read_csv(fichier)

# Envoyer le rappel
def envoyer_rappel(contact, sujet, message):
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = contact
    msg['Subject'] = sujet

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(email_address, email_password)
    text = msg.as_string()
    server.sendmail(email_address, contact, text)
    server.quit()

# Vérifier les rendez-vous et envoyer des rappels
def verifier_et_rappeler(rendez_vous):
    for index, rdv in rendez_vous.iterrows():
        date_rdv = datetime.strptime(rdv['date'], '%Y-%m-%d %H:%M:%S')
        if date_rdv - datetime.now() <= timedelta(days=1):
            envoyer_rappel(rdv['contact'], "Rappel de Rendez-vous", "N'oubliez pas votre rendez-vous demain à " + rdv['heure'])

def main():
    rendez_vous = lire_rendez_vous('rendez_vous.csv')
    verifier_et_rappeler(rendez_vous)

if __name__ == '__main__':
    main()
