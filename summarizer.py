# Importing modules
from urllib import request
import re
import nltk
#nltk.download('punkt')
import heapq

#Summarizer function
def summarize(text , no_of_sentence):

    #Cleaning the text
    text = re.sub(r'\[[0-9]*\]', ' ',text)
    text = re.sub(r'\s+', ' ',text)

    # Tokenize the sentence from text
    sentence_token = nltk.sent_tokenize(text)

    # Removing punctuations etc -> Cleaning text
    text = re.sub(r'[^a-zA-Z]', ' ',text)
    text = re.sub(r'\s+', ' ',text)

    # Create word token
    word_tokens = nltk.word_tokenize(text)

    # Remove stop words and calculate frequencies
    stopwords = nltk.corpus.stopwords.words('english') 

    #Initializing word_frequency dictionary
    word_frequencies = {} 

    #Loop through all the words in word token
    for word in word_tokens:

        #Omit stopwords
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    #Get maximum word frequency
    maximum_frequency = max(word_frequencies.values())

    #Normalize word frequencies
    for word in word_frequencies.keys():
        word_frequencies[word] =  (word_frequencies[word]/maximum_frequency)

    # Calculate sentence score with each word weigthed frequency
    sentence_scores = {}

    #Loop through all sentence tokens and calculate sentence score
    for sentence in sentence_token:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_frequencies.keys():
                if (len(sentence.split(' '))) < 30 :
                    if sentence not in sentence_scores.keys():
                        sentence_scores[sentence] =  word_frequencies[word]
                    else: 
                        sentence_scores[sentence] +=  word_frequencies[word]

    #Get the top 'no_of_sentence' sentences
    summary_text = heapq.nlargest(no_of_sentence,sentence_scores,key=sentence_scores.get)

    return summary_text



# Using Web Scraping to get breif on an article in wikipedia
'''
from bs4 import BeautifulSoup as bs
url = "https://en.wikipedia.org/wiki/Machine_learning"
    allParagraphContentSummary = ""

    htmlDoc = request.urlopen(url)

    soupObject = bs(htmlDoc , 'html.parser')
    paragraphContents = soupObject.findAll('p')
    #print(paragraphContent)

    for paragraphContent in paragraphContents:
        allParagraphContentSummary += paragraphContent.text 
'''