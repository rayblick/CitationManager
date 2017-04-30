# Custom libraries
import sys
sys.path.append('..')
from generic import helpers as gh
from bibtex import helpers as bh

# Existing libraries
import glob
import pandas as pd
from wordcloud import WordCloud
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

class Bibtex(object):

    def __init__(self):
        self.original_words = []
        self.stemmed_words = []
        self.metadata = []
        self.docformat = ""


    def process_citations(self, docpath, docformat):
        self.docformat = docformat
        self.metadata, self.stemmed_words, self.original_words = bh.process_citations_handle(docpath, docformat)


    def predict_citation_label(self, testpath='data/test', pattern='stemmed', targetlabelname='journal'):
        # create labels
        if pattern == "original":
            idtrain, ylabels, xdata = gh.create_labels(self.original_words, targetlabelname)
        else:
            idtrain, ylabels, xdata = gh.create_labels(self.stemmed_words, targetlabelname)

	# Create array of counts
        vec = DictVectorizer()
        xtrain = vec.fit_transform(xdata)

        # transform by freq and fit
        tf_transformer = TfidfTransformer()
        xtrain_tf = tf_transformer.fit_transform(xtrain)
  
        # prepare test data
        md, sd, od = bh.process_citations_handle(testpath, self.docformat)
        print("NB: the same doc format is assumed from the training data: {}".format(self.docformat))
        # need to handle exceptions: no abstract
        idtest, ytest, xtest = gh.create_labels(od, targetlabelname)

        # transform test
        xtest = vec.transform(xtest)
        xtest_tf = tf_transformer.transform(xtest)

        # fit train and predict test data
        clf = MultinomialNB().fit(xtrain_tf, ylabels)
        predicted = clf.predict(xtest_tf)
        
        # print
        df = ([y for y in zip(idtest, ytest, [x for x in predicted])])
        resultsDF = pd.DataFrame(df, columns=['URL','journal','predicted'])
        return pd.merge(md,resultsDF, left_on=['URL','journal'], right_on=['URL','journal'])

