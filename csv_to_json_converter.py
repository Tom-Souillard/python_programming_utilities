import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    data = []
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Utilisation
# csv_to_json('chemin/vers/fichier.csv', 'chemin/vers/fichier.json')
