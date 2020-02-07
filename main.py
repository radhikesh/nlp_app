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
        data = request.form['link']
    if 'http' in data:
        webarticle_data = urllib.request.urlopen(data)
        webarticle = webarticle_data.read()
        parsed_webarticle = bs.BeautifulSoup(webarticle, 'lxml')
        webarticle_text = parsed_webarticle.find_all('p')
        article = ""
        for p in webarticle_text:
            article += p.text
    elif data == "":
        return render_template('result2.html')
    elif len(data.split()) < 200:
        return render_template('result3.html')
    else:
        article = data

    # pre-processing:

    # removing square brackets and extra spaces:
    article = re.sub(r'\[[0-9]*\]', ' ', article)
    article = re.sub(r'\s+', ' ', article)

    # removing special characters and digits:

    cleaned_article = re.sub('[^a-zA-Z]', ' ', article)
    cleaned_article = re.sub(r'\s+', ' ', cleaned_article)

    # we use formatted article text:
    sentence_list = nltk.sent_tokenize(article)

    # creating weighted frequency:
    stopwords = nltk.corpus.stopwords.words('english')
    word_frequencies = {}

    for word in nltk.word_tokenize(cleaned_article):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    max_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word] / max_frequency)

    # calculating sentence scores:

    sentence_scores = {}

    for sentence in sentence_list:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_frequencies.keys():
                if len(sentence.split(' ')) < 30:
                    if sentence not in sentence_scores.keys():
                        sentence_scores[sentence] = word_frequencies[word]
                    else:
                        sentence_scores[sentence] += word_frequencies[word]

    article_summary = heapq.nlargest(5, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(article_summary)
    return render_template('result.html', summary=summary)


if __name__ == '__main__':
    app.run(debug=True)
