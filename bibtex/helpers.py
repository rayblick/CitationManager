"""
Helpers to parse bibtex citations.
"""
import re
import sys
sys.path.append('..')
from generic import helpers as gh

def bibtex_splitter(file):
    """
    Summary
    --------
    Helper function to splitter text document into citation articles
    and process hard coded parameters. The input txt file needs to be
    a set of citations downloaded in Bibtex format. There are specific
    patterns that are looked for to split the text document such as
    the @article value to separate the primary content. Returns a list
    of dictionaries containing all of the keywords defined in this method.

    Parameters
    -----------
    arg1: txt file

    Usage
    -----
    text = open('data/more_citations.txt', 'r')
    bibtex_splitter(text)

    Example data
    -------------


    Returns
    ---------

    """
    # Placeholder
    textcapture = []

    # List of items to collect
    items = ['ISSN =', 'URL =','abstract =', 'author =', 'journal =', 'number =',
         'pages =', 'publisher =', 'title =', 'volume =', 'year =']

    # Loop over the file (txt file)
    for doc in file.read().split('@'):
        temp = {}
        for item in items:
            m = re.search(item, doc)
            try:
                item_end = doc[m.end(): ]
                capture = item_end[item_end.find('{') + 1 : item_end.find('}')]
                temp[item[:-2]] = capture

            except:
                pass

        # Add list
        textcapture.append(temp)

    return textcapture



def process_citations_handle(docpath, docformat):
    """Parse documents containing bibtex citations."""

    # placeholders
    original_words = []
    stemmed_words = []
    metadata = []

    # collect documents
    docs = gh.doc_finder_handle(docpath, docformat)

    # loop over docs
    for each_file in docs:

        # open text file
        text = open(each_file, 'r', encoding="utf8")

        # split text
        bs = bibtex_splitter(text)

        # read in each article
        for article in bs:

            # skip if no data
            if article == {}:
                continue

            else:
                try:
                    # temp palce holder
                    temp = []

                    # Convert string to words dictionary
                    output_text = gh.word_cleaning_handle(article['abstract'])

                    # Drop stopwords and apply stemming
                    originalwords, stemmedwords = gh.remove_stopwords(output_text)

                    # collect article attibutes
                    #article.pop('abstract', None)
                    if article['abstract'] != {}:
                        article['abstract'] = "Y"

                    # Append results
                    original_words.append([article, originalwords])
                    stemmed_words.append([article, stemmedwords])

                except:
                    pass

                finally:
                    # Append results
                    metadata.append(article)

    # Drop duplicates
    metadata = gh.deduplicate_dictionary(metadata)
    stemmed_words = gh.deduplicate_listoflists(stemmed_words)
    original_words = gh.deduplicate_listoflists(original_words)

    # Create table for article details
    metadata = gh.list_of_dictionaries_to_dataframe(metadata)

    # Return results
    return metadata, stemmed_words, original_words
