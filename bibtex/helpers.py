"""
Helpers to parse bibtex citations.
"""
import re

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
    items = ['ISSN =', 'abstract =', 'author =', 'journal =', 'number =', 
         'pages =', 'publisher=', 'title=', 'volume=', 'year=']
    
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



