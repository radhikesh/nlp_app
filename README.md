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


