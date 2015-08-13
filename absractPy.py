import glob
import timeit
import re

# create function to clean up the text
# this gets applied in the main function
def read_bibtex(string_of_text):
    dictionary_of_words ={}
    regex = re.compile("[%()^$0-9,'\.;:!?{}]")
    
    for word in string_of_text.split(' '):
    
        # implement regex from above for each word
        m = regex.sub('', word)
        
        # drop spaces and single letters 
        if len(m) > 1:
            # note the use of lower case | add words to dictionary
            dictionary_of_words[m.lower()] = dictionary_of_words.get(m.lower(),0)+1
            
    return dictionary_of_words


# main function   
from wordcloud import STOPWORDS
import Stemmer
#import pandas as pd
#import math
#df = pd.DataFrame() # too slow with many files... use dictionary instead

stemmed_journal_words = {}
original_journal_words = {}

stemmer = Stemmer.Stemmer('english')

# find all the text documents in the root directory
# note that there are specific requirements to find the appropriate text
# see the bit of code below referring to -> 'abstract = {}'
docs = []
for each_file in glob.glob("*.txt"):
    docs.append(each_file)
number_of_docs = len(docs)
document_counter = 0

# add timer
tic = timeit.default_timer()
word_counter = 0

for each_file in docs:
    # add one to the document counter to show progress
    document_counter += 1
    # provide running count down in console
    print 'working on... %s (%s/%s)' %(each_file, document_counter, number_of_docs)
    
    # open text file
    text = open(each_file,'r') 
    
    # read in each line
    for i in text.readlines():
        
        # strip white space etc
        line = i.strip()
        # find all the lines starting with abstract
        if re.search(r'^abstract', line):
            # skip if an abstract is missing - signifyed by {empty}
            if re.search(r'abstract = {}', line):
                continue
            else:
                # strip beginning and end of the abstract
                # Be warned this is manual process: changes in Bibtex output
                # could effect the words at the start and end of the abstract
                line = line[13:-2]
                
                # use the function read_bibtex to get a dictionary of words 
                # without syntax defined above with regex compile
                output_text = read_bibtex(line)
                
                # pull key-value pairs from dictionary and parse out stopwords
                for key, value in output_text.items():
                    if re.search(r'\\', key) or key in STOPWORDS:
                        pass
                    else:    
                        # need to use stem package to remove plurals
                        try:    
                            key_stem = stemmer.stemWord(key)
                        except:
                            # if the stemming algorithm fails... add in the original word
                            stemmed_journal_words[key] = stemmed_journal_words.get(key.lower(),0) + value
                        
                        # to add word count to the console
                        word_counter += value
                        
                        # compile the new dictionary by increasing the re-occurring values across years
                        stemmed_journal_words[key_stem] = stemmed_journal_words.get(key_stem.lower(),0) + value
                        original_journal_words[key] = original_journal_words.get(key_stem.lower(),0) + value
                        
                        # THIS IS VERRRRY SLOW....
                        #df = df.append({'year': each_file[0:4], 
                                        #'orig_word':key,
                                        #'stem_word': key_stem, 
                                        #'count': value},ignore_index=True)
    
    # Finished file - add elapsed time
    toc=timeit.default_timer()
    time_estimator = round(toc-tic,2)/(float(document_counter)/float(number_of_docs))
    print 'Elapsed time: %s sec; Number of words counted: %s; Time to complete: %s sec' %(round(toc-tic,1),word_counter,round(time_estimator,1))

    
#print journal_words           
