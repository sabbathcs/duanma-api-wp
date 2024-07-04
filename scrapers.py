import requests
from bs4 import BeautifulSoup

class ScrapeTools:
    user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0'}
    max_page = 1
    def __init__(self):
        pass

   
    
class AssistanceDogsInternational(ScrapeTools):
    def __init__(self):
        pass

    def run_scrape():
        url = 'https://assistancedogsinternational.org/news/member-news'
        a_urls = set()
        r = requests.get(url, headers = ScrapeTools.user_agent)
        while True:
            soup = BeautifulSoup(r.text, 'html.parser')
            div_posts = soup.find('div', {'class':'main-lister'})

            h4_posts = div_posts.find_all('h4')

            for h4_post in h4_posts[0: ScrapeTools.max_page]:
                a_url = h4_post.find('a')
                a_url = a_url.get('href')
                a_url = f'https://assistancedogsinternational.org/{a_url}'
                a_urls.add(a_url)
                print(a_url)
            try:
                pageLinkNext = soup.find('a', text=lambda x: x and 'Next >>' in x)
                pageLinkNext = pageLinkNext.get('href')
                pageLinkNext = f'https://assistancedogsinternational.org/' + pageLinkNext
                r = requests.get(pageLinkNext, headers = ScrapeTools.user_agent)
            except:
                break

        """
        Captura los links de las paginas y las guarda en a_urls. Hay que realizar que entre y guarde la noticia
        """

class TherapyDogs(ScrapeTools):
    def __init__(self):
        pass

    def run_scrape():
        url = 'https://www.therapydogs.com/atd-blog/'
        a_urls = set()
        r = requests.get(url, headers = ScrapeTools.user_agent)
        while True:
            soup = BeautifulSoup(r.text, 'html.parser')
            div_posts = soup.find('div', {'class':'fusion-blog-shortcode'})
            articles_posts = div_posts.find_all('article')

            for article in articles_posts:
                h2 = article.find('h2')
                a_href = h2.find('a')
                a_href = a_href.get('href')
                print(a_href)
                a_urls.add(a_href)
            
            try:
                a_next_button = soup.find('a', {'class':'pagination-next'})
                a_next_button = a_next_button.get('href')
                r = requests.get(a_next_button, headers = ScrapeTools.user_agent)
            except:
                print('No se encontro boton next')
                break

        """
        Captura los links, y los guarda en a_urls. Hacer que ingrese a las url y capture las noticias.
        """

class TheWildEst(ScrapeTools):
    def __init__(self):
        pass

    def run_scrape():
        url = 'https://www.thewildest.com/'
        a_urls = set()
        r = requests.get(url, headers = ScrapeTools.user_agent)
        soup = BeautifulSoup(r.text, 'html.parser')

        h3s = soup.find_all('h3', {'class':'F_d3'})
        for h3 in h3s:
            a_url = h3.find('a')
            a_url = a_url.get('href')
            a_url = f'https://www.thewildest.com{a_url}'
            a_urls.add(a_url)
            print(a_url)
    """
    Captura los links de los articulos, y los guarda en a_urls. Hacer que se ingrese y se guarde la informacion del articulo
    """


class Dogster(ScrapeTools):
    def __init__(self):
        pass

    def run_scrape():
        url = 'https://www.dogster.com/'
        a_urls = set()
        r = requests.get(url, headers = ScrapeTools.user_agent)
        data = {}
        soup = BeautifulSoup(r.text, 'html.parser')
        div_articles = soup.find_all('div', {'class':'article-text'})
        for article in div_articles[0: ScrapeTools.max_page]:
            h3 = article.find('h3')
            a_href = h3.find('a')
            a_href = a_href.get('href')
            print(a_href)
            a_urls.add(a_href)
        for a_url in a_urls:
            r = requests.get(a_url, headers = ScrapeTools.user_agent)
            soup = BeautifulSoup(r.text, 'html.parser')
            main_article = soup.find('main', {'id':'main'})
            if (author_content := main_article.find('div', {'class': 'pangolia-toc'})):
                author_content.decompose()
            if (article_author := main_article.find('div', {'class':'article-author'})):
                article_author.decompose()
            title_article = soup.find('h1', {'class':'the-title'}).text
            data_article = main_article.find('div', {'class':'entry-content'}).text


            data = {'Titulo':title_article,
                    'Articulo':data_article,
                    'Url': a_url}
            print(title_article, data_article)


        
        return data
    """
    Captura los links de los articulos, y los guarda en a_urls. Hacer que se ingrese y se guarde la informacion del articulo
    """

'''class ModernDogMagazine(ScrapeTools):
    def __init__(self):
        pass
    
    def run_scrape():
        url = 'https://www.dogster.com/'
        a_urls = set()
        r = requests.get(url, headers = ScrapeTools.user_agent)

        soup = BeautifulSoup(r.text, 'html.parser')
        div_articles = soup.find('div', {'class':'latest-articles-aside'})
        
        articles = div_articles.find_all('div', {'class':'mpi-title'})
        for article in articles:
            '''