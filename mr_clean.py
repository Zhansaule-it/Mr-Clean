# install lxml
# install nltk
from bs4 import BeautifulSoup
import requests
from nltk.tokenize import word_tokenize
import re
from collections import Counter
import matplotlib.pyplot as plt
from operator import itemgetter 

def remove_stop_words(words, stop_words):
    without_stop_words = {}
    for word in words:
        if word not in stop_words:
            without_stop_words[word] = words[word]
    return without_stop_words

def vizualize(collection):
    sorted_dict = {}
    sorted_keys = sorted(collection, key=collection.get) 
    for w in sorted_keys:
        sorted_dict[w] = collection[w]
    plt.barh(list(sorted_dict.keys()),list(sorted_dict.values()))  
    plt.title('Most Common Tokens in the Ozon layer article') 
    plt.show() 

def print_most_frequent(frequencies, n):
    out = dict(sorted(frequencies.items(), key = itemgetter(1), reverse = True)[:n]) 
    print(out)
    return out

def count_frequency(collection):
    return Counter(collection)

def lower_collection(collection):
    return [x.lower() for x in collection]

def tokenize(content):
    return word_tokenize(content)

def merge_contents(data):
    pattern2 =  r"\[.*\]"
    data = re.sub(pattern2," ", data)
    pattern = r"[^\w]"
    data = re.sub(pattern," ", data)
    return data

def get_content(article_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    data = []
    art = soup.find_all('p')
    for tag in art:
        data.append(tag.text)
    data_str = "".join(data)
    return data_str

url = 'https://en.wikipedia.org/wiki/Ozone_layer'
get_content(url)
data = get_content(url)
merge_content = merge_contents(data)
collection = tokenize(merge_content)
collection = lower_collection(collection)
frequencies = count_frequency(collection)
print("\n10 most frequent words: ")
m_frequencies = print_most_frequent(frequencies, 10)
print("\n20 most frequent words with vizualization: ")
m_frequencies = print_most_frequent(frequencies, 20)
vizualize(m_frequencies)
#removing stopwords
stop_words = [ "the", "a", "of", "to", "in", "about", "and","is","by","are", "less","than","while","because","at","for","be","on","this","these","have","with","which","as","that","from","was","it", "all","its","has","can", "most", "were","an", "over","being","other","out", "or","s","000","b","c","100","200","9", "although", "5"]
filtered_collection = remove_stop_words(frequencies, stop_words)
print("\n25 most frequent words without stopwords: ")
m_frequencies = print_most_frequent(filtered_collection, 25)
vizualize(m_frequencies)
