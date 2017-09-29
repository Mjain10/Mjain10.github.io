from textblob import TextBlob
from tools import *

def length_tuples(text:TextBlob):
    '''returns a list of two tuples (# of sentence, length of sentence)'''
    return [(i+1,len(text.sentences[i].words)) for i in range(len(text.sentences))]

def redundant_words(text:TextBlob):
    '''returns a list of two tuples (# of sentence, no of redundant words)'''
    set_of_redundant_words = {'absolutely', 'actual', 'add', 'advance', 'back', 'basic', 'brief', 'careful', 'close',
                              'completely', 'constantly', 'difficult', 'down', 'entirely', 'fellow', 'final', 'first',
                              'full', 'live', 'major', 'new','nearly', 'old', 'over', 'past', 'personal', 'pre',
                              'safe', 'since', 'small', 'still', 'together', 'truely', 'unexpected', 'unintentional',
                              'very'}
    return [(i+1,len(set_of_redundant_words.intersection(set([j for j in text.sentences[i].words])))) for i in range(len(text.sentences))]


def repeating_words(text:TextBlob):
    '''returns a list of two tuples (# of sentence, no of repeating words)'''
    result = list()
    for i in range(len(text.sentences)):
        count = 0
        for n in sorted(text.sentences[i].word_counts.values(), reverse = True):
            if n > 1:
                count += 1
        result.append((i+1, count))
    return result
    #return [(i+1, 1) for i in range(len(text.sentences)) if sorted(text.sentences[i].word_counts.values(), reverse = True)[0] > 1]

def points_by_length(text:TextBlob):
    '''Calculates points by length and returns a list of two tuples (# of sentence, no of points)'''
    pass

# if __name__ == '__main__':
    ##For testing
    # print(length_tuples(TextBlob('I am Amitesh. This is a summarization project.')))
    # print(repeating_words(TextBlob('This is a check for redundant words and redundant phrases phrases. Being redundant is is redundant. This is not a repeating sentence')))
    # print(redundant_words(TextBlob('This is absolutely and completely neccessary. It was a very unintentional phenonmenon')))
