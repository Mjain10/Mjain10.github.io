#This module is for identifying topic, first, and last sentences of a paragraph and giving them higher points for the final summary

from processdoc import ProcessDoc,Textblob_with_file_name
from high_frequency_words import high_frequency_words
from project_tools import *

def identify_first(text:Textblob_with_file_name):
    '''Identifies the first sentence of each paragraph and returns it as a list of two tuples i.e (# of paragraph, first sentence)'''
    first = list()
    for para in range(len(text.document.all_paragraphs())):
        if len(text.document.all_paragraphs()[para].sentences) > 0:
            first.append((para + 1, str(text.document.all_paragraphs()[para].sentences[0])))
    return first

def identify_last(text:Textblob_with_file_name):
    '''Identifies the last sentence of each paragraph and returns it as a list of two tuples i.e (# of paragraph, last sentence)'''
    last = list()
    for para in range(len(text.document.all_paragraphs())):
        if len(text.document.all_paragraphs()[para].sentences) > 0:
            last.append((para + 1, str(text.document.all_paragraphs()[para].sentences[-1])))
    return last

def identify_topic(text:Textblob_with_file_name):
    '''Identifies the topic sentence(s) of each paragraph and returns it as a list of two tuples i.e (# of paragraph, topic sentence) if present'''
    frequent_words = high_frequency_words(text.document.convert_to_textblob())
    topic = list()
    for para in range(len(text.document.all_paragraphs())):
        for sentence in text.document.all_paragraphs()[para].sentences:
            if len(set(sentence.words).intersection(frequent_words)) > 0:
                topic.append((para + 1, str(sentence)))
    return topic

def points_by_topic_first_last(text:Textblob_with_file_name):
    '''Calculates points by the first, last, and topic sentences and returns a list of two tuples (# of sentence, no of points)'''
    doc = text.document


# if __name__ == '__main__':
#     ##For testing
#     doc = Textblob_with_file_name('Reflective Introduction.docx')
#     print(identify_first(doc))
#     print(identify_last(doc))
#     print(identify_topic(doc))
