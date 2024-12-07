from flask import Flask, request, jsonify
from recommendation_engine import recommend_items, movies, books

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    item_type = data['type']
    title = data['title']

    if item_type == 'movie':
        recommendations = recommend_items(movies, title)
    elif item_type == 'book':
        recommendations = recommend_items(books, title)
    else:
        return jsonify({"error": "Invalid type"}), 400

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
