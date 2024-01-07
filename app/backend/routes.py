from app.backend import backend
from flask import jsonify, request
from flask_cors import cross_origin
import requests
from app.backend.forms import Bible

@backend.route('/', methods=['GET', 'POST'])
@cross_origin(headers=['Content-Type'])
def home():
    RandomVerseUrl = 'https://bible-api.com/?random=verse'
    RandomVerseResponse = requests.get(RandomVerseUrl)
    RandomVerseData = RandomVerseResponse.json()

    randomVerseText = RandomVerseData['verses'][0]['text']
    randomVerse = RandomVerseData['verses'][0]['verse']
    RandomChapter = RandomVerseData['verses'][0]['chapter']
    RandomBook = RandomVerseData['verses'][0]['book_name']
    reference = RandomVerseData['reference']

    return jsonify( randomVerse=randomVerse,
                    randomVerseText=randomVerseText,
                    RandomChapter=RandomChapter,
                    RandomBook=RandomBook,
                    reference=reference,)

@backend.route('/search', methods=['GET', 'POST'])
@cross_origin(headers=['Content-Type'])
def bibleSearch():
    form = Bible()

    if request.method == 'POST':
        search = form.bible_search.data

        url = f'https://bible-api.com/{str(search)}'
        response = requests.get(url)
        data = response.json()

        try:
            text = data['text']
            verse = data['verses'][0]['verse']
            chapter = data['verses'][0]['chapter']
            book = data['verses'][0]['book_name']
            reference = data['reference']

            return jsonify( verse=verse,
                        text=text,
                        chapter=chapter,
                        book=book,
                        reference=reference)
        except IndexError:
            return ("This is a bug")

    else:
        return ("This did not work")