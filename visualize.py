import pandas as pd
import matplotlib.pyplot as plt

# Lire le fichier CSV
df = pd.read_csv("sentiment_analysis_results.csv")

# Compter combien de sentiments de chaque type
sentiment_counts = df["Sentiment"].value_counts()

# Afficher en camembert (pie chart)
plt.figure(figsize=(6, 6))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("distribución de sentimientos")
plt.axis('equal')
plt.show()

# Afficher aussi en barres
plt.figure(figsize=(6, 4))
sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'])
plt.title("Número de comentarios por sentimiento")
plt.xlabel("Sentimiento")
plt.ylabel("Número de comentarios")
plt.grid(axis='y')
plt.show()
