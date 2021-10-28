#Data Preparation Exercises



import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd

import acquire


def basic_clean(string):
    
    # This function does basic cleaning and prepping of a string
    
    #Lowercase all text in string
    prepped_string = string.lower()   
    
    #Normalize unicode letters
    prepped_string = unicodedata.normalize('NFKD', prepped_string)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore') 
    
    # remove anything that is not a through z, a number, a single quote, or whitespace
    prepped_string = re.sub(r"[^a-z0-9'\s]", '', prepped_string)

    return prepped_string
    

def tokenize(string):
    
    import nltk
    from nltk.tokenize.toktok import ToktokTokenizer
    
    #This function takes in a string and tokenizes all the words in the string.
    
    tokenizer = nltk.tokenize.ToktokTokenizer()
    
    return (tokenizer.tokenize(string, return_str=True))



def stem(text):
    
    #Import library
    import nltk
    
    # This function accepts some text and returns the text after applying stemming to all the words.
    
    # Create the nltk stemmer object, then use it
    ps = nltk.porter.PorterStemmer()
    
    stems = [ps.stem(word) for word in text.split()]
    text_stemmed = ' '.join(stems)
    
    return text_stemmed    

