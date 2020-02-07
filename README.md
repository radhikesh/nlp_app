# University of Illinois Chicago NLP app

------

### Steps followed to create the app:
- Web scraping
  - Extracted the text from the article url using urllib and beautifulsoup library.
  - Parsed the extracted text using lxml parser.
- Pre-processing
  - Removed special characters and digits
  - Removed extra white spaces
  - tokenizing the article into different sentences
- Article Summary using nltk library
  - Calculated the frequency of occurrence of each word except the stopwords (like is, and,the)
  - Calculated the weighted frequency which is the ratio of frequency of each word over the frequency of the most
       occurring word.
  - Calculated the sentence score by adding the weighted frequency for each word.
  - Selected the top 5 sentences with the highest scores.
- App deployment:
  - Used flask library to convert the above process into an app
  - Deployed the app on GCP's (google cloud platform) app engine
  - Check out the app [here][]

<!-- external links -->
[here]:https://text-summarizer-nlp-app.appspot.com/


