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


    def process_citations(self, docpath='../data/bibtex/train', docformat='txt'):
        self.docformat = docformat
        self.metadata, self.stemmed_words, self.original_words = bh.process_citations_handle(docpath, docformat)


    def predict_citation_label(self, testpath='../data/bibtex/test',
            pattern='stemmed', targetlabelname='journal'):

        # prepare test data
        md, sd, od = bh.process_citations_handle(testpath, self.docformat)

        # create identifiers, labels and data
        if pattern == "original":
            idtrain, ylabels, xdata = gh.create_labels(self.original_words, targetlabelname)
            idtest, ytest, xtest = gh.create_labels(od, targetlabelname)
        else:
            idtrain, ylabels, xdata = gh.create_labels(self.stemmed_words, targetlabelname)
            idtest, ytest, xtest = gh.create_labels(sd, targetlabelname)

	    # Create array of counts
        vec = DictVectorizer()
        xtrain = vec.fit_transform(xdata)
        xtest = vec.transform(xtest)

        # transform by freq and fit
        tf_transformer = TfidfTransformer()
        xtrain_tf = tf_transformer.fit_transform(xtrain)
        xtest_tf = tf_transformer.transform(xtest)

        # fit train and predict test data
        clf = MultinomialNB().fit(xtrain_tf, ylabels)
        predicted = clf.predict(xtest_tf)

        # print setup
        df = ([y for y in zip(idtest, ytest, [x for x in predicted])])
        resultsDF = pd.DataFrame(df, columns=['URL', targetlabelname, 'prediction'])

        # reutrn dataframe
        return pd.merge(md, resultsDF, left_on=['URL', targetlabelname], right_on=['URL', targetlabelname])
