# University of Illinois Chicago text summarizer app using NLP

------

There are two main methods to summarize the text:
1. Extraction based summarization:
   Creating summary by extracting major sentences from the article and combining them together.
2. Abstraction based summarization:
   It creates new sentences that convey the useful information from the original text.

For this task I used the first technique that is extraction based summarization.

### Steps followed to create the app:
- Web scraping
  - Extracted the text from the article url using urllib and beautifulsoup library
  - Parsed the extracted text using lxml parser
- Pre-processing
  - Removed special characters and digits
  - Removed extra white spaces
  - Tokenized the article into different sentences
- Article Summary using nltk library
  - Calculated the frequency of occurrence of each word except the stopwords (like is, and, the)
  - Calculated the weighted frequency which is the ratio of frequency of each word over the frequency of the most
       occurring word
  - Calculated the sentence score by adding the weighted frequency for each word
  - Selected the top 5 sentences with the highest scores
- App deployment:
  - Used flask library to convert the above process into an app
  - Deployed the app on GCP's (google cloud platform) app engine
  - The app takes any article link or the article itself as the input to create the summary
  - The article must be atleast 200 words
  - I tested the app with the following uic news article but it's general enough to work with any news article
    - https://today.uic.edu/uic-student-launches-late-night-talk-show
    - https://today.uic.edu/bringing-the-farm-to-the-dining-halls
  - Check out the app [here][]
  - Code is in main.py [file][]

<!-- external links -->
[file]:https://github.com/radhikesh/nlp_app/blob/master/main.py
[here]:https://text-summarizer-nlp-app.appspot.com/


