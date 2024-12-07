import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Load datasets
movies = pd.read_csv('movies.csv')  # Replace with the path to your movie dataset
books = pd.read_csv('books.csv')   # Replace with the path to your book dataset

def recommend_items(data, item_title, top_n=5):
    count_vectorizer = CountVectorizer()
    matrix = count_vectorizer.fit_transform(data['description'])  # Use relevant text field
    similarity = cosine_similarity(matrix)

    item_idx = data[data['title'] == item_title].index[0]
    scores = list(enumerate(similarity[item_idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    recommendations = [data.iloc[i[0]]['title'] for i in scores[1:top_n + 1]]
    return recommendations

