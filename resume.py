import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def resume_article(data):
    Titulo, Articulo, Url = data.values()
    article_split = Articulo.split('.')
    article_split = [item for item in article_split if item.strip()]
    print(len(article_split))
    featurizer = TfidfVectorizer(
        stop_words = stopwords.words('spanish'),
        norm='l1',
    )
    X = featurizer.fit_transform(article_split)
    print(X)
    '''
    Separa en oraciones, y los vectoriza, luego los tengo que separar
    '''