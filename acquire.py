# Data Acquisition / Web Scraping Exercises

import requests
from bs4 import BeautifulSoup
import pandas as pd 
import os

# Create a function to read all articles and create a dictionary containing the title and content of each article from Code Up blogs

def parse_article(article):
    
    #title
    title  = article.select('.entry-title')[0].text
    
    #content
    content = article.select('.et_pb_module.et_pb_post_content.et_pb_post_content_0_tb_body')[0].text.strip()
    
    return {'title': title, 'content': content}


# Create a function that takes a list of Code Up blog urls and parses the articles from them and creates a dictionary with 
# title and content of each article

def get_blog_articles():

    urls = ['https://codeup.com/data-science/codeups-data-science-career-accelerator-is-here/',
        'https://codeup.com/data-science/data-science-myths/',
        'https://codeup.com/data-science/data-science-vs-data-analytics-whats-the-difference/',
        'https://codeup.com/data-science/10-tips-to-crush-it-at-the-sa-tech-job-fair/',
        'https://codeup.com/data-science/competitor-bootcamps-are-closing-is-the-model-in-danger/']
    
    filename = "blogs.csv"

    if os.path.isfile(filename):

       return pd.read_csv(filename)

    else:

        for url in urls:
            
            if url == urls[0]:
            
                response = requests.get(url, headers={'user-agent': 'Codeup DS Germain'})
                soup = BeautifulSoup(response.text)
            
                #Get the articles from the web page
                articles = soup.select('.et_pb_section.et_pb_section_0_tb_body.et_section_regular')
            
                article = articles[0]
            
                df = pd.DataFrame([parse_article(article) for article in articles])   
                
            
            else: 
                
                response = requests.get(url, headers={'user-agent': 'Codeup DS Germain'})
                soup = BeautifulSoup(response.text)
            
                #Get the articles from the web page
                articles = soup.select('.et_pb_section.et_pb_section_0_tb_body.et_section_regular')
            
                article = articles[0]  
                
                df = df.append(pd.DataFrame([parse_article(article) for article in articles]), ignore_index=True)

                df.to_csv(r'blogs.csv', index=False)
            
        return df


# Create a function to read all articles and create a dictionary containing the title and content of each article

def parse_news_article(article, category):
    
    #title
    title  = article.find('span',itemprop="headline").text
    
    #author
    author = article.find('span', 'author').text
    
    #content
    content = article.find('div',itemprop="articleBody").text.strip()
    
    #category
    category = category
    
    
    
    return {'title': title, 'author':author, 'content': content,'category': category}


# Create a function that takes a list of categories for inshorts website and parses the articles from them and creates a dictionary with 
# title, author, and  content of each article

def get_news_articles(categories):

    filename = "news.csv"

    if os.path.isfile(filename):

       return pd.read_csv(filename)

    else:

        url = 'https://inshorts.com/en/read/'
        
        for category in categories:
            
            if category == categories[0]:
            
                response = requests.get(url+category, headers={'user-agent': 'Codeup DS Germain'})
                soup = BeautifulSoup(response.text)
            
                #Get the articles from the web page
                articles = soup.select('.news-card.z-depth-1')
            
                article = articles[0]
            
                df = pd.DataFrame([parse_news_article(article, category) for article in articles])   
                
            
            else: 
                
                response = requests.get(url+category, headers={'user-agent': 'Codeup DS Germain'})
                soup = BeautifulSoup(response.text)
            
                #Get the articles from the web page
                articles = soup.select('.news-card.z-depth-1')
            
                article = articles[0]  
                
                df = df.append(pd.DataFrame([parse_news_article(article, category) for article in articles]), ignore_index=True)

                df.to_csv(r'news.csv', index=False)
            
        return df