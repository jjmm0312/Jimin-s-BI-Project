import nltk
import requests
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk import FreqDist
from nltk.corpus import stopwords
from bs4 import BeautifulSoup as bs

import math
import random
import json
import re
import pandas

import numpy as np


def data_process(data):
    '''
    fname = 'new_list.json'

    data = []
    with open(fname, 'r') as f:
        data = json.load(f)
    '''
    jCheck = 0
    corpus = []
    #print(len(data))

    for i in range(len(data)):
        print(i)
        #print(json.dumps(data[i], indent="\t"))
        index = i
        category = data[i]['category']
        short_description = data[i]['short_description']
        headline = data[i]['headline']
        short_description = short_description.lower()
        headline = headline.lower()


        url = data[i]['link']
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = requests.get(url, headers=headers)
        soup = bs(req.content, 'html.parser')

        news_data = []

        for link in soup.find_all('p'):
            news_data.append(link.text.strip())
        # print(news_data)
        news_description = ", ".join(news_data)



        short_description = data[i]['short_description']
        headline = data[i]['headline']
        short_description = short_description.lower()
        headline = headline.lower()
        news_description = news_description.lower()
        news_description = news_description.replace(",", "")


        shortword = re.compile(r'\W*\b\w{1,2}\b')

        short_description = shortword.sub('', short_description)
        headline = shortword.sub('', headline)


        short_description = re.sub('[!@#$%^&“”*",('')/<>?.=]', '', short_description)
        short_description = short_description.replace("]", "")
        short_description = short_description.replace("[", "")
        short_description = short_description.replace("-", "")

        headline = re.sub('[!@#$%^&*,('')"“”/<>?.=]', '', headline)
        headline = headline.replace("]", "")
        headline = headline.replace("[", "")
        headline = headline.replace("-", "")

        news_description = shortword.sub('', news_description)
        news_description = re.sub('[!@#$%^&*,('')“”"/<>?.=]', '', news_description)
        news_description = news_description.replace("]", "")
        news_description = news_description.replace("[", "")
        news_description = news_description.replace("-", "")
        news_description = news_description.replace("_", "")



        stop = stopwords.words('english')

        tokens1 = nltk.word_tokenize(short_description)
        tokens2 = nltk.word_tokenize(headline)

        tokens1 = [word for word in tokens1 if not word in stop]
        tokens2 = [word for word in tokens2 if not word in stop]

        news_token = nltk.wordpunct_tokenize(news_description)
        news_token = [word for word in news_token if not word in stop]


        tokens = tokens1 + tokens2 + news_token



        lm = WordNetLemmatizer()
        lm_tokens = [lm.lemmatize(w, pos = "v") for w in tokens]
        #print("lemmatizing : ", lm_tokens)

        tagged_list = pos_tag(lm_tokens)
        pnouns_tokens = [t[0] for t in tagged_list if t[1] == "NNP"]
        nouns_tokens = [t[0] for t in tagged_list if t[1] == "NN"]
        verb_tokens = [t[0] for t in tagged_list if t[1] == "VB"]

        token_list = pnouns_tokens + nouns_tokens + verb_tokens
        #print(token_list)

        freq_list = FreqDist(token_list)
        freq_word = freq_list.most_common(3)
        if(i%1000 == 0):
            print("frequency of word : ", freq_word)

        news_word_tag = ""
        for i in range(3):
            try:
                for j in range(freq_word[i][1]):
                    news_word_tag += " " + freq_word[i][0]
            except IndexError:
                continue
        news_word_tag = news_word_tag.lstrip()
        dict_corpus = {'index': index, 'category': category, 'news_word_tag': news_word_tag}
        corpus.append(dict_corpus)

    with open('corpus.json', 'w') as fout:
        json.dump(corpus, fout, indent="\t")

    return corpus
