from flask import Flask, jsonify, request
from flask_cors import CORS
from scrapers import *
from translate import translate_article

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['POST'])
def post_data():
    '''data = Dogster.run_scrape()
    data_translate = translate_article(data)'''
    data = {'Titulo':'Am I a Helicopter Dog Parent? Ways I May Be Overprotective of Penny ',
            'Articulo':'The 4 Ways I Might Be Overprotecting Penny: 1. I Don’t Let Strangers Pet Her… at All Is this being a helicopter dog parent, or is this common sense? Penny is not what you would call a friendly dog… at least to people she doesn’t know. She’s very protective of her family, and she has shown her teeth before to people that have gotten too close to us while we’re out with her. Because of this, I don’t let strangers pet her at all. I’m afraid she’s going to nip at somebody. Her bark is definitely worse than her bite, but if she nips at the wrong person, they may try to sue me or something, especially if there is a child involved. In the rare event that I do let someone pet her, I always give them a warning first that she doesn’t like strangers. But it’s better to be safe than sorry and just avoid letting people pet her altogether. I’m even thinking about getting her one of those harnesses or bandanas that says “do not pet.” Then if someone tries to pet her, it’s their own fault. 2. I Don’t Let Her Go Outside by Herself Our street is not super busy with traffic, and she’s never once left our yard. All she does is just sit in the driveway and watch cars go by. But I still won’t let her go outside by herself. I think this is totally rational since our front yard doesn’t have a fence.',
            'Url': 'https://es.wikipedia.org/wiki/Al_romper_el_alba'}
    data_resume = resume_article(data)
    return jsonify(data_resume), 201

if __name__ == '__main__':
    app.run(debug=True)