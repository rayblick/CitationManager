import glob
from wordcloud import WordCloud
import sys
sys.path.append('..')
from generic import helpers as gh
from bibtex import helpers as bh
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

class Bibtex(object):

    def __init__(self):
        self.original_words = []
        self.stemmed_words = []
        self.metadata = []
        self.docformat = ""


    def process_citations_handle(self, docpath, docformat):
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
                        #article.pop('abstract', None)
                        if article['abstract'] != {}:
                            article['abstract'] = "Y"
					    
					    # Append results
                        original_words.append([article, originalwords])
                        stemmed_words.append([article, stemmedwords])
					    
                    except:
                        pass

					# Append results
                    metadata.append(article)    

        # Drop duplicates
        metadata = gh.deduplicate_dictionary(metadata) 
        stemmed_words = gh.deduplicate_listoflists(stemmed_words)   
        original_words = gh.deduplicate_listoflists(original_words)

        # Create table for article details
        metadata = gh.list_of_dictionaries_to_dataframe(metadata)        
        return metadata, stemmed_words, original_words


    def process_citations(self, docpath, docformat):
        self.docformat = docformat
        self.metadata, self.stemmed_words, self.original_words = self.process_citations_handle(docpath, docformat)


    def predict_data(self, testpath, data, targetlabelname):
        # create labels
        ylabels, datadictionary = gh.create_labels(data, targetlabelname)

		# Create array of counts
        vec = DictVectorizer()
        xtrain = vec.fit_transform(datadictionary)

        # transform by freq and fit
        tf_transformer = TfidfTransformer()
        xtrain_tf = tf_transformer.fit_transform(xtrain)
  
        # prepare test data
        md, sd, od = self.process_citations_handle(testpath, self.docformat)
        ytest, xtest = gh.create_labels(od, targetlabelname)

        # transform test
        xtest = vec.transform(xtest)
        xtest_tf = tf_transformer.transform(xtest)

        # fit and predict
        clf = MultinomialNB().fit(xtrain, ylabels)
        predicted = clf.predict(xtest_tf)
        
        # print
        print(predicted)

