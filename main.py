from flask import Flask
import bs4 as bs
from flask import Flask, render_template, url_for, request
import urllib.request
import re
import nltk as nltk
nltk.download('punkt')
import heapq
nltk.download('stopwords')
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return "About page"


@app.route("/model", methods=['POST'])
def model():
    # data extraction:
    if request.method == 'POST':
        link = request.form['link']
    scrapped_data = urllib.request.urlopen(link)
    article = scrapped_data.read()

    parsed_article = bs.BeautifulSoup(article, 'lxml')

    paragraphs = parsed_article.find_all('p')

    article_text = ""

    for p in paragraphs:
        article_text += p.text

    # pre-processing:

    # removing square brackets and extra spaces:
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)

    # removing special characters and digits:

    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

    # we use formatted article text:
    sentence_list = nltk.sent_tokenize(article_text)

    # creating weighted frequency:
    stopwords = nltk.corpus.stopwords.words('english')
    word_frequencies = {}

    for word in nltk.word_tokenize(formatted_article_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word] / maximum_frequency)

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

    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentences)
    return summary


if __name__ == '__main__':
    app.run(debug=True)
