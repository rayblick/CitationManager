"""
Generic helpers not specific to one citation style.
"""
import glob
from nltk.stem.snowball import SnowballStemmer
import re
from wordcloud import STOPWORDS


# Add stemmer
stemmer = SnowballStemmer("english")
stemmer.stem("Running")

def doc_finder_handle(basepath, fileformat):
    """
    Finds files of a particular format in the basepath.
    """
    # place holder
    docs = []

    # Loop over files
    for each_file in glob.glob(basepath + '/*.' + fileformat):
        docs.append(each_file)

    # return docs
    return docs


def word_cleaning_handle(string_of_text):
    """
    Converts a string to a dictionary of words. 
    
    Parameters
    -----------
    arg1: string
    
    Usage
    ------
    word_cleaning_handle('this test')
    
    Returns
    --------
    {'this': 1, 'test': 1}
    
    Doctest
    --------
    >>> word_cleaning_handle('text65[12];:')
    {'text': 1}
    """
    # Empty dictionary
    dictionary_of_words ={}
    
    # Regex to process each word
    regex = re.compile("[%()^$0-9,'\.;:!?{}\]\[]")
    
    # loop over a string split by whitespace
    for word in string_of_text.split(' '):
    
        # implement regex from above for each word
        m = regex.sub('', word)
        
        # drop spaces and single letters 
        if len(m) > 1:
            # note the use of lower case | add words to dictionary
            dictionary_of_words[m.lower()] = dictionary_of_words.get(m.lower(), 0) + 1
            
    # Return the results
    return dictionary_of_words


def remove_stopwords(dictionary):
    # Placeholder for output
    stemmed_journal_words = {}
    original_journal_words = {}
    
    # pull key-value pairs from dictionary and parse out stopwords
    for key, value in dictionary.items():

        # pass on all stop words
        if re.search(r'\\', key) or key in STOPWORDS:
            pass

        else:    
            try: 
                # Add stemmed word 
                key_stem = stemmer.stem(key)
                stemmed_journal_words[key_stem] = stemmed_journal_words.get(
                    key_stem.lower(), 0) + value

            except:
                # If stemming fails enter the original word
                stemmed_journal_words[key] = stemmed_journal_words.get(
                    key.lower(), 0) + value

            finally:        
                # Add in original words        
                original_journal_words[key] = original_journal_words.get(
                    key.lower(), 0) + value
                
    return original_journal_words, stemmed_journal_words


def deduplicate_dictionary(listofdictionaries):
    """
    Removes duplicate dictionaries in a list.
    """
    return [dict(tupleized) for tupleized in set(tuple(item.items()) for item in listofdictionaries)]
