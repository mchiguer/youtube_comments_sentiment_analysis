import csv
from textblob import TextBlob
import matplotlib.pyplot as plt

# Charger les commentaires depuis un fichier .txt
with open("comments_clean.txt", "r", encoding="utf-8") as file:
    comments = file.readlines()

# Nettoyage basique des commentaires
comments = [comment.strip().lower() for comment in comments]  # Retirer les espaces et convertir en minuscules
# Fonction pour analyser les sentiments des commentaires
def analyze_sentiment(comments):
    sentiments = []
    for comment in comments:
        blob = TextBlob(comment)
        sentiment = blob.sentiment.polarity  # Score de polarité
        if sentiment > 0:
            sentiments.append('Positive')
        elif sentiment < 0:
            sentiments.append('Negative')
        else:
            sentiments.append('Neutral')
    return sentiments

# Appliquer l'analyse de sentiment
sentiments = analyze_sentiment(comments)

# Sauvegarder les résultats dans un fichier .csv
with open("sentiment_analysis_results.csv", mode="w", newline="", encoding="utf-8") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["Commentaire", "Sentiment"])  # Écrire les en-têtes du fichier CSV

    for comment, sentiment in zip(comments, sentiments):
        writer.writerow([comment, sentiment])  # Écrire chaque commentaire et son sentiment

print("Les résultats de l'analyse de sentiment ont été sauvegardés dans 'sentiment_analysis_results.csv'.")
