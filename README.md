# University of Illinois Chicago NLP app

------

### Steps followed to create the app:
- Web scraping
    - Extract the text from the article url using urllib and beautifulsoup library.
    - Parse the extracted text using lxml parser.

- Pre-processing
    - removing special characters and digits
    - removing extra white spaces
    - tokenizing the article into different sentences

- Creating text Summary using nltk library
    - calculate the frequency of occurrence of each word except the stopwords (like is, and,the)
    - then calculated the weighted frequency which is ratio of frequency of each word over the frequency of the most
       occurring word.
    - calculated the sentence score by adding the weighted frequency for each word.
    - selected the top 5 sentences with the highest scores.

- App deployment:
    - Used flask library to convert the above process into an app
    - Deployed the app on GCP's (google cloud platform) app engine
    - Check out the app [here][]

<!-- external links -->
[here]:https://text-summarizer-nlp-app.appspot.com/


