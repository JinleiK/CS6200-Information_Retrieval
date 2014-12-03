__author__ = 'jinlei'

import sys
import collections
from BM25 import BM25
from DocStatistics import DocStatistics


class RunBM25:
    system_name = "jinlei"

    def __init__(self, index, queries, docnum):
        # the queries dictionary fetched from the queries input file
        self.queries = fetch_queries(queries)
        # number of documents
        self.docNum = docnum
        # the documents statistics constructed from the data in inverted index list file
        self.docSta = DocStatistics(index)

    # calculate all the BM25 scores for all the queries in the queries file
    def cal_bm25(self):
        self.docSta.fetch_inverted()
            #print("query_id" + '\t' + "Q0" + '\t' + "doc_id" + '\t' + "rank"
            #  + '\t' + "BM25_score" + '\t' + "system_name")
        for qid, q in self.queries.items():
            bm25 = BM25(self.docSta, q)
            bm25.cal_scores()
            self.print_scores(qid, bm25)

    # output the required number of sorted document scores for a query in the required format
    def print_scores(self, qid, bm25):
        # record the rank of the document
        count = 1
        for doc, score in bm25.sorted_scores[:int(self.docNum)]:
            print(str(qid) + "\t" + "Q0" + '\t' + str(doc) + '\t' + str(count)
                  + '\t' + str(score) + '\t' + RunBM25.system_name)
            count += 1


# fetch all the queries from the queries file
def fetch_queries(queryfile):
    queries = {}
    f = open(queryfile)
    while True:
        line = f.readline().strip('\n')
        if len(line) == 0:
            break
        query = line.split('\t')
        # query ID : query TEXT
        queries[query[0]] = query[1]
    f.close()
    # sort the queries for output
    return collections.OrderedDict(sorted(queries.items()))

if __name__ == '__main__':
    if len(sys.argv) == 4:
        run = RunBM25(sys.argv[1], sys.argv[2], sys.argv[3])
        run.cal_bm25()
    else:
        print("Usage: BM25 <index file> <queries> <num of doc results>")