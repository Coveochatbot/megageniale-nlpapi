from nltk import word_tokenize
from nltk.corpus import stopwords
import re
import heapq

LANGUAGE = 'french'
additionalStopWords = ['je', 'tu', 'il', 'nous', 'vous', 'ils', 'salut', 'bye', 'ça', 'genre', 'chose']


class QueryParser(object):
    def __init__(self, word_model):
        self.model = word_model

    def parseText(self, text):
        words = word_tokenize(text, language=LANGUAGE)
        regex = re.compile('[^a-zA-Z0-9éÉàèìòùÀÈÌÒÙçÇâêîôûÂÊÎÔÛ]')
        words = [regex.sub('', w).lower() for w in words]
        words = [w for w in words if w]
        return words


    def parse_query(self, sentence):
        words = self.parseText(sentence)
        print('Step 1: split query in words', words)
        stopWords = set(stopwords.words(LANGUAGE))
        for w in additionalStopWords:
            stopWords.add(w)
            print('adding ' + w + ' to stop words')
        words = [word for word in words if word not in stopWords]
        print('Step 2: remove stopwords', words)
        word_tuples = [(self.model[w], w) for w in words if w in self.model]
        heapq.heapify(word_tuples)
        print('Step 3: sort by rarity', word_tuples)
        rarest_words = [w[1] for w in heapq.nlargest(5, word_tuples)]
        print('Step 4: keep most frequents', rarest_words)
        return " ".join(rarest_words)
