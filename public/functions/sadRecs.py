from flask import Flask, jsonify
import requests

app = Flask(__name__)

GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"
API_KEY = 'AIzaSyCFDaqjpgA8K_NqqCw93xorS3zumc_52u8'

@app.route('/api/adventure-books')
def get_adventure_books():
    adventure_keywords = ['adventure', 'exploration', 'journey', 'quest', 'expedition', 'danger', 'thrilling']
    adventure_books = []

    for keyword in adventure_keywords:
        response = requests.get(GOOGLE_BOOKS_API_URL, params={'q': keyword, 'key': API_KEY})
        if response.status_code == 200:
            books_data = response.json()
            books = books_data.get('items', [])
            adventure_books.extend(books)

    books_output = [{
        'title': book['volumeInfo'].get('title', 'No Title'),
        'authors': book['volumeInfo'].get('authors', []),
        'description': book['volumeInfo'].get('description', ''),
        'thumbnail': book['volumeInfo'].get('imageLinks', {}).get('thumbnail', '')
    } for book in adventure_books]

    return jsonify(books_output)

if __name__ == "__main__":
    app.run(debug=True)