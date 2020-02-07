from app import app
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
        data = request.form['input']
    if 'http' in data:
        print("Yes")
        webarticle_data = urllib.request.urlopen('https://today.uic.edu/novel-coronavirus-update-feb-4-2020')
        webarticle = webarticle_data.read()
        parsed_webarticle = bs.BeautifulSoup(webarticle, 'lxml')
        webarticle_text = parsed_webarticle.find_all('p')
        article = ""
        for p in webarticle_text:
            article += p.text
    else:
        article2 = 'Dear students, faculty and staff,We are writing today to update you about the novel coronavirus.  We acknowledge that there may be uncertainty around this rapidly changing situation and we recognize that there may be concern or anxiety, particularly for those who have family or friends in China or elsewhere who are directly impacted. During times like this, inaccurate and insensitive information can spread widely on social media and online.  Your wellbeing is our utmost concern and we encourage all members of the campus community to support each other. As more information has become available about the 2019 novel coronavirus, the Centers for Disease Control and Prevention (CDC) has updated guidance for all travelers to limit activities for 14 days after travel from mainland China. This includes people who do not have symptoms of illness and people who were exposed to a person with confirmed novel coronavirus. Limitation of activities includes staying home, avoiding public activities and not attending classes. The University has worked to identify students that are known to have traveled from China and determine if any of these students have symptoms. The majority of our students that have traveled from China have been back on campus for more than 14 days and we are not aware of any that have presented symptoms. However, there may be a few students or employees who have traveled from China that we are not aware of, so we will remain vigilant and help to identify anyone who might be at risk for the novel coronavirus and try to prevent transmission to others. Currently, there are no known cases of novel coronavirus that have been identified in the UIC community. We encourage anyone who has traveled to China and is having respiratory symptoms to contact a health care provider.If a faculty member or student has traveled in the last 14 days from mainland China, they should not attend classes or work and should call for guidance on self-monitoring and limitation of activities.Students can contact Student Health at University Village at 312-996-2901 for health-related guidance. Students who may need additional support and assistance during this ongoing situation should contact the U and I Care program, an initiative of the Office of the Dean of Students.Employees should contact University Health Service at 312-996-7420 during business hours (Monday, Tuesday, Thursday and Friday 7 a.m.-4 p.m. and Wednesday 7 a.m.-3 p.m.)Additional resources are available at the University of Illinois Hospital by calling 866-600-CARE (2273).In addition, we advise students, faculty and staff to avoid travel to China in recognition of the U.S. State Department’s “Do Not Travel” advisory. It is now flu season. This is a higher risk to our campus community currently.  We recommend anyone who is sick with any respiratory illness to stay home from work or classes and consider an evaluation with their health care provider.  People should wash their hands often, for 20 seconds, to help prevent the spread of viruses, including flu. Please know, it is not too late to get a flu shot.'

    # pre-processing:

    # removing square brackets and extra spaces:
    article = re.sub(r'\[[0-9]*\]', ' ', article)
    article = re.sub(r'\s+', ' ', article)

    # removing special characters and digits:

    cleaned_article = re.sub('[^a-zA-Z]', ' ', article)
    cleaned_article = re.sub(r'\s+', ' ', cleaned_article)

    # we use formatted article text:
    sentence_list = nltk.sent_tokenize(article)
    sentence_list_new = article.split(sep=".")
    article2 = 'Dear students, faculty and staff,We are writing today to update you about the novel coronavirus.  We acknowledge that there may be uncertainty around this rapidly changing situation and we recognize that there may be concern or anxiety, particularly for those who have family or friends in China or elsewhere who are directly impacted. During times like this, inaccurate and insensitive information can spread widely on social media and online.  Your wellbeing is our utmost concern and we encourage all members of the campus community to support each other. As more information has become available about the 2019 novel coronavirus, the Centers for Disease Control and Prevention (CDC) has updated guidance for all travelers to limit activities for 14 days after travel from mainland China. This includes people who do not have symptoms of illness and people who were exposed to a person with confirmed novel coronavirus. Limitation of activities includes staying home, avoiding public activities and not attending classes. The University has worked to identify students that are known to have traveled from China and determine if any of these students have symptoms. The majority of our students that have traveled from China have been back on campus for more than 14 days and we are not aware of any that have presented symptoms. However, there may be a few students or employees who have traveled from China that we are not aware of, so we will remain vigilant and help to identify anyone who might be at risk for the novel coronavirus and try to prevent transmission to others. Currently, there are no known cases of novel coronavirus that have been identified in the UIC community. We encourage anyone who has traveled to China and is having respiratory symptoms to contact a health care provider.If a faculty member or student has traveled in the last 14 days from mainland China, they should not attend classes or work and should call for guidance on self-monitoring and limitation of activities.Students can contact Student Health at University Village at 312-996-2901 for health-related guidance. Students who may need additional support and assistance during this ongoing situation should contact the U and I Care program, an initiative of the Office of the Dean of Students.Employees should contact University Health Service at 312-996-7420 during business hours (Monday, Tuesday, Thursday and Friday 7 a.m.-4 p.m. and Wednesday 7 a.m.-3 p.m.)Additional resources are available at the University of Illinois Hospital by calling 866-600-CARE (2273).In addition, we advise students, faculty and staff to avoid travel to China in recognition of the U.S. State Department’s “Do Not Travel” advisory. It is now flu season. This is a higher risk to our campus community currently.  We recommend anyone who is sick with any respiratory illness to stay home from work or classes and consider an evaluation with their health care provider.  People should wash their hands often, for 20 seconds, to help prevent the spread of viruses, including flu. Please know, it is not too late to get a flu shot.'

    article2 = re.sub(r'\[[0-9]*\]', ' ', article2)
    article2 = re.sub(r'\s+', ' ', article2)

    # removing special characters and digits:

    cleaned_article2 = re.sub('[^a-zA-Z]', ' ', article2)
    cleaned_article2 = re.sub(r'\s+', ' ', cleaned_article2)

    # we use formatted article text:
    sentence_list2 = nltk.sent_tokenize(article2)


    # creating weighted frequency:
    stopwords = nltk.corpus.stopwords.words('english')
    word_frequencies = {}

    for word in nltk.word_tokenize(cleaned_article):
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
    return summary


if __name__ == '__main__':
    app.run(debug=True)






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
    return render_template('result.html', summary=summary)