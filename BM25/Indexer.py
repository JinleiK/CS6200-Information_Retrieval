__author__ = 'jinlei'

import sys


class Document:
    def __init__(self, doc_id):
        # document id
        self.doc_id = doc_id
        # the numbers of tokens in the document
        self.tokens_nums = {}


class Indexer:
    def __init__(self, inpath, outpath):
        # file path of corpus
        self.corpus = inpath
        # output file path
        self.index = outpath
        # documents with words frequency (tf)
        self.docs = []
        # the inverted list
        self.inverted_list = {}

    # fetch docs and their contents from the corpus file
    def fetch_docs(self):
        f = open(self.corpus)
        while True:
            line = f.readline().strip('\n')
            if len(line) == 0:
                break
            # get the doc id, then create a new document object, and it to the docs list
            if line.startswith('#'):
                doc_id = int(line[1:].strip())
                doc = Document(doc_id)
                self.docs.append(doc)
            # count all the words frequency and store in the document object
            else:
                words = line.split(" ")
                # the latest added document
                doc = self.docs[-1]
                count = 0
                for w in words:
                    w = w.strip()
                    if len(w) == 0:
                        continue
                    count += 1
                    if w not in doc.tokens_nums:
                        doc.tokens_nums[w] = 1
                    else:
                        doc.tokens_nums[w] += 1

    # build inverted list based on the constructed doc data
    def invert_list(self):
        for doc in self.docs:
            for w, tf in doc.tokens_nums.items():
                if w not in self.inverted_list:
                    self.inverted_list[w] = []
                self.inverted_list[w].append([doc.doc_id, tf])

    # write the index list to the output file
    def output_index(self):
        f = open(self.index, "w")
        for w, index_list in self.inverted_list.items():
            f.write(w + ' ')
            for tf in index_list:
                # f.write(str(tf) + ' ')
                f.write(str(tf[0]) + ' ')
                f.write(str(tf[1]) + ' ')
            f.write('\n')
        f.close()

    # def output_doclen(self):
    #     f = open("doclen.txt", 'w')
    #     dl_sum = 0
    #     for doc in self.docs:
    #         f.write(str(doc.doc_id) + ' ')
    #         f.write(str(doc.dl) + '\n')
    #         dl_sum += doc.dl
    #     self.avdl = float(dl_sum) / len(self.docs)
    #     f.write(str(self.avdl))
    #     f.close()

    # for test
    def print_doc(self):
        for doc in self.docs[:20]:
            print(doc.doc_id)
            for k, v in doc.tokens_nums.items():
                print(k, v)

    # for test
    def print_list(self):
        for k, v in self.inverted_list.items():
            print(k, v)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        indexer = Indexer(sys.argv[1], sys.argv[2])
        indexer.fetch_docs()
        indexer.invert_list()
        indexer.output_index()
