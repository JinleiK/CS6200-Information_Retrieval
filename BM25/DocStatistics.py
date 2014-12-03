__author__ = 'jinlei'


class DocStatistics:
    def __init__(self, filepath):
        # file path of doc statistics
        self.file = filepath
        # terms dictionary to store their frequencies in docs
        self.terms = {}
        # doc lengths dictionary
        self.doclens = {}
        # average length of all docs
        self.avdl = 0
        # number of documents
        self.docN = 0

    # fetch the inverted index list from the input file
    def fetch_inverted(self):
        f = open(self.file)
        while True:
            line = f.readline().strip('\n')
            if len(line) == 0:
                break
            tokens = line.split(' ')
            # record the first word of the line as the term
            self.terms[tokens[0]] = {}
            # add the rest of the line to the term dictionary
            for i in range(1, len(tokens) - 1, 2):
                # doc id
                doc = tokens[i]
                # term frequency
                tf = int(tokens[i + 1])
                self.terms[tokens[0]][doc] = tf
                if doc not in self.doclens:
                    self.doclens[doc] = 0
                # accumulate the length of doc
                self.doclens[doc] += tf
        f.close()
        self.docN = len(self.doclens)
        self.calculate_avg()

    # calculate the average doc length
    def calculate_avg(self):
        dl_sum = 0
        for doc, dl in self.doclens.items():
            dl_sum += dl
        self.avdl = float(dl_sum) / len(self.doclens)