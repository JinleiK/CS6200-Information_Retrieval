__author__ = 'jinlei'

import math
import operator


class BM25:
    # constant parameters
    k1 = 1.2
    k2 = 100
    b = 0.75
    qf = 1
    r = 0
    R = 0

    def __init__(self, docs, query):
        # document statistics
        self.docs = docs
        # query
        self.query = query
        # document scores for the query
        self.scores = {}
        # sorted document scores for output
        self.sorted_scores = {}

    # calculate the scores of all the documents for the query
    def cal_scores(self):
        terms = self.query.split(' ')
        for term in terms:
            inverted_list = self.docs.terms[term]
            n = len(inverted_list)
            for docid, tf in inverted_list.items():
                if docid not in self.scores:
                    self.scores[docid] = 0.0
                # calculate all the factors respectively
                factor1 = ((BM25.r+0.5)/(BM25.R-BM25.r+0.5)) / ((n-BM25.r+0.5)/(self.docs.docN-n-BM25.R+BM25.r+0.5))
                factor2 = (BM25.k1+1)*tf / (self.cal_k(docid)+tf)
                factor3 = (BM25.k2+1)*BM25.qf / (BM25.k2+BM25.qf)
                score = math.log(factor1) * factor2 * factor3
                self.scores[docid] += score
        # sort the scores of all the documents
        self.sorted_scores = sorted(self.scores.items(), key=operator.itemgetter(1), reverse=True)

    # calculate the K
    def cal_k(self, docid):
        dl = self.docs.doclens[docid]
        return BM25.k1 * ((1-BM25.b) + BM25.b*dl/self.docs.avdl)
