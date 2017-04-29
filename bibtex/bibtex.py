import glob
from wordcloud import WordCloud
import sys
sys.path.append('..')
from generic import helpers as gh
from bibtex import helpers as bh

class Bibtex(object):

    def __init__(self):
        self.original_words = []
        self.stemmed_words = []
        self.article_details = []


    def process_citations(self, docpath, docformat):
        """Parse documents containing bibtex citations."""

        # collect documents
        docs = gh.doc_finder_handle(docpath, docformat)

		# loop over docs
        for each_file in docs:

			# open text file
            text = open(each_file, 'r') 
	
			# split text
            bs = bh.bibtex_splitter(text)

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
                        article.pop('abstract', None)
					    
					    # Append results
                        self.original_words.append([article, originalwords])
                        self.stemmed_words.append([article, stemmedwords])
					    
                    except:
                        pass

					# Append results
                    self.article_details.append(article)                



        

