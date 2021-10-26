




import requests
from bs4 import BeautifulSoup

#Function to parse thru HTML news article and return title, date and author
def parse_news_article(article):
    title = article.h2.text
    date, author = article.select('.italic')[0].find_all('p')
    return {'title': title, 'date': date.text, 'author': author.text}


    
response = requests.get('https://web-scraping-demo.zgulde.net/news')
soup = BeautifulSoup(response.text)
articles = soup.select('.grid.gap-y-12 > div')
pd.DataFrame([parse_news_article(article) for article in articles])