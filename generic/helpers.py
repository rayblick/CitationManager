"""
Generic helpers not specific to one citation style.
"""
import glob
from nltk.stem.snowball import SnowballStemmer
import re
from wordcloud import STOPWORDS
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

# Add stemmer
stemmer = SnowballStemmer("english")
stemmer.stem("Running")

def doc_finder_handle(basepath, fileformat):
    """
    Finds files of a particular format in dir that is given in basepath.

    Parameters
    ----------
    arg1: String defining a file path
    arg2: String defining document format 

    Default args
    ------------
    None

    Exceptions
    ----------
    None

    Usage
    -----
    # add test.txt to data/test dir
    doc_finder_handle(data/test, 'txt')

    Returns
    -------
    ['text.txt']

    Doctest
    -------
    None

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
    ----------
    arg1: string

    Default args
    ------------ 
    None

    Exceptions
    ----------
    None
    
    Usage
    ------
    word_cleaning_handle('this test')
    
    Returns
    -------
    {'this': 1, 'test': 1}
    
    Doctest
    -------
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
    """
    Removes single letters (e.g. 'a') and stop words (e.g. 'the').

    Parameters
    ----------
    arg1: dictionary of word-count pairs

    Exceptions
    ----------
    Try to stem each word. Exception returns the original word.

    Usage
    -----
    remove_stopwords({'running': 5})

    Returns
    -------
    Two dictionaries; 
        1) original words 
        2) stemmed words
    ({'running': 5}, {'run': 5})

    Doctest
    -------
    >>> remove_stopwords({'this':1, 'running':5, 'testing': 2})
    ({'running': 5, 'testing': 2}, {'run': 5, 'test': 2})

    """
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

    Parameters
    ----------
    arg1: list containing dictionaries

    Exceptions
    ----------
    None

    Usage
    -----
    # list
    list_of_dictionaries = [{'dict1': 2}, 
                            {'dict1': 2}, 
                            {'dict2': 3}]
    # run
    deduplicate_dictionary(list_of_dictionaries)

    Returns
    -------
    No order is assumed in the output
    [{'dict1': 2}, {'dict2': 3}]

    Doctest
    -------
    >>> deduplicate_dictionary([{'test': 2}, {'test': 2}])
    [{'test': 2}]

    """
    return [dict(tupleized) for tupleized in set(tuple(item.items()) for item in listofdictionaries)]


def deduplicate_listoflists(listoflists):
    """
    Remove double ups in lists.

    Parameters
    ----------
    arg1: list of lists

    Exceptions
    ----------
    None

    Usage
    -----
    deduplicate_listoflists([['test'], 
                             ['test']])

    Returns
    -------
    [['test']]

    Doctest
    -------
    >>> deduplicate_listoflists([[1,2], [1,2]])
    [[1, 2]]
    
    """
    temp=[]
    for i in listoflists:
        if i not in temp:
            temp.append(i)
    return temp


def list_of_dictionaries_to_dataframe(data):
    """
    Uses the first dictionary keys to build the headers.
    Then appends all data to the df.

    Parameters
    ----------
    arg1: list of dictionaries

    Exceptions
    ----------
    None

    Usage
    -----
    list_of_dictionaries_to_dataframe([{'Field': 'Science', "Issue": 1}, 
                                       {'Field': 'Art', "Issue": 23}])

    Returns
    -------
    pandas dataframe

    output =
    ---------------------------------
    |   ID  |    Field    |  Issue  |
    ---------------------------------
    |   0   |    Science  |   1.0   |
    |   1   |    Art      |   23.0  |
    ---------------------------------


    Mismatch Error
    --------------
    If dictionary keys dont match then ne columns are generated in the output
    Example,
    list_of_dictionaries_to_dataframe([{'Field': 'Science', "Issue": 1}, 
                                       {'Topic': 'Art', "Issue": 23}]) 
    output =
    -------------------------------------------
    |   ID  |    Field    |  Issue  |  Topic  |
    -------------------------------------------
    |   0   |    Science  |   1.0   |  NaN    |
    |   1   |    NaN      |   23.0  |  Art    |
    -------------------------------------------


    Doctest
    -------
    None

    """
    myDF = pd.DataFrame(columns = data[0].keys())
    for citation in data:
        myDF = myDF.append(citation, ignore_index=True)
    return myDF


def create_labels(data, labelname):
    """
    Generates labels, data and identifier fields for analysis.    

    Parameters
    ----------
    arg1: List of lists, each list contains 2 dictionaries.
    arg2: String specifying a key to use as labels 

    Exceptions
    ----------
    None

    Usage
    -----
    data = [
            [{'URL': 'fake@email.com',
              'journal': 'Ecology',
              'title': 'Home ranges of a bird'},
             {'aerial': 1,
              'aim': 1,
              'area': 1,
              'assemblages': 1}],

            [{'URL': 'fake2@email.com',
              'journal': 'Biology',
              'title': 'Invasion of a rat'},
             {'cover': 1,
              'toxic': 1,
              'prey': 1,
              'predator': 1}]
           ]
    
    create_labels(data, 'journal')

    Returns
    -------
    Three lists each in the order of processing.
        1) identifier (list)
        2) labelname (list)
        3) word counts (dictionary) 

    (['fake@email.com', 'fake2@email.com'],
     ['Ecology', 'Biology'],
     [{'aerial': 1, 'aim': 1, 'area': 1, 'assemblages': 1},
      {'cover': 1, 'predator': 1, 'prey': 1, 'toxic': 1}])

    Doctest
    -------
    None
    
    """
    ylabels = []
    identifier = []
    xdicts = []

    for i in range(len(data)):
        label = data[i][0][labelname]
        ylabels.append(label)
        identifier.append(data[i][0]["URL"])
        xdicts.append(data[i][1])

    return identifier, ylabels, xdicts



