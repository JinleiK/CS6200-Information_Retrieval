__author__ = 'callie'

import math
import operator


class PageRank:
    def __init__(self, graph):
        self.graph = graph
        self.N = len(graph.all_nodes)
        self.d = 0.85
        self.PR = dict()
        # perplexities for latest four iterations
        self.perplexities = [None, None, None, None]
        self.counter = 0

    def rank(self, file_size):
        new_pr = dict()

        for n in self.graph.all_nodes:
            self.PR[n] = 1 / float(self.N)
        while not self.converged(file_size):
            # derive the perplexity first
            perp = self.perplexity()
            # update the perplexity list
            self.perplexities.pop(0)
            self.perplexities.append(perp)
            # output perplexity value obtained in each round for the in-links file
            if file_size == "big":
                print perp

            sink_pr = 0
            for s in self.graph.sink_nodes:
                sink_pr += self.PR[s]
            for n in self.graph.all_nodes:
                new_pr[n] = (1-self.d) / self.N
                new_pr[n] += self.d * sink_pr / self.N
                for m in self.graph.in_links[n]:
                    # print m
                    # print self.graph.out_links[m]
                    # print self.PR[m]
                    if m in self.PR:
                        new_pr[n] += self.d * self.PR[m] / self.graph.out_links[m]
            for n in self.graph.in_links.keys():
                self.PR[n] = new_pr[n]
            self.counter += 1
            # list the PageRank values obtained for each of the six vertices
            # after 1, 10, and 100 iterations of the PageRank algorithm
            if file_size == "small" and (self.counter == 1 or self.counter == 10 or self.counter == 100):
                print "Iteration", self.counter
                for n, p in self.PR.items():
                    print n + ":", p

        return self.PR

    def converged(self, file_size):
        if None in self.perplexities:
            return False

        if file_size == "small" and self.counter <= 100:
            return False

        if file_size == "big":
            for i in range(1, len(self.perplexities)):
                if self.perplexities[i] - self.perplexities[i - 1] >= 1.0:
                    return False
        return True

    def perplexity(self):
        return math.pow(2, self.entropy())

    def entropy(self):
        h = 0
        for n, p in self.PR.items():
            h += p * math.log(p, 2)
        return -h

    def sort_by_inlink(self):
        in_link_counts = dict()
        for k, v in self.graph.in_links.items():
            in_link_counts[k] = len(v)
        sort(in_link_counts[:50])


def sort(dictionary):
    sorted_nodes = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
    print_pages(sorted_nodes[:50])


def print_pages(nodes):
    for k, v in nodes:
        print k + ":", v