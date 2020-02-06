import pandas as pd
import numpy as np

from flask import Flask, render_template, url_for, request
import pickle

import bs4 as bs
import urllib.request
import re

#data extraction:
scrapped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')
article = scrapped_data.read()

parsed_article = bs.BeautifulSoup(article, 'lxml')

paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:
    article_text += p.text

#pre-processing:

#removing square brackets and extra spaces:
article_text = re.sub(r'\[[0-9]*\]' , ' ', article_text)
article_text = re.sub(r'\s+',' ', article_text)

#removing special characters and digits:

formatted_article_text = re.sub('[^a-zA-Z]',' ', article_text)
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

# we use formatted article text:
import nltk as nltk
nltk.download('punkt')
sentence_list = nltk.sent_tokenize(article_text)

#creating weighted frequency:
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')
word_frequencies = {}

for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] +=1

maximum_frequency = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

# calculating sentence scores:

sentence_scores = {}

for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

import heapq

summary_sentences = heapq.nlargest(7, sentence_scores, key = sentence_scores.get)

summary = ' '.join(summary_sentences)
print(summary)
