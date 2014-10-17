__author__ = 'callie'

import math
import operator


class PageRank:
    def __init__(self, graph):
        self.graph = graph
        # number of all pages
        self.N = len(graph.all_nodes)
        # pagerank damping factor
        self.d = 0.85
        # pagerank values for each page
        self.PR = dict()
        # count the iterations that change in perplexity is less than 1
        self.perp_counter = 0
        # count the total iterations
        self.counter = 0

    def rank(self, file_size):
        # record the previous perplexity value
        pre_perp = 0.0
        new_pr = dict()

        for n in self.graph.all_nodes:
            self.PR[n] = 1.0 / self.N

        while not self.converged(file_size):
            # derive the perplexity first
            cur_perp = self.perplexity()

            if abs(cur_perp - pre_perp) < 1.0:
                self.perp_counter += 1
            else:
                self.perp_counter = 0

            # output perplexity value obtained in each round for the in-links file
            if file_size == "big":
                print(cur_perp)

            sink_pr = 0.0
            for s in self.graph.sink_nodes:
                sink_pr += self.PR[s]
            for n in self.graph.all_nodes:
                new_pr[n] = (1.0-self.d) / self.N
                new_pr[n] += self.d*sink_pr / self.N
                for m in self.graph.in_links[n]:
                    new_pr[n] += self.d * self.PR[m] / self.graph.out_links_count[m]
            for n in self.graph.all_nodes:
                self.PR[n] = new_pr[n]
            self.counter += 1
            pre_perp = cur_perp
            # list the PageRank values obtained for each of the six vertices
            # after 1, 10, and 100 iterations of the PageRank algorithm
            if file_size == "small" and (self.counter == 1 or self.counter == 10 or self.counter == 100):
                print("Iteration", self.counter)
                for n, p in self.PR.items():
                    print(n + ":", p)

        return self.PR

    def converged(self, file_size):
        if file_size == "small" and self.counter <= 100:
            return False

        if file_size == "big" and self.perp_counter < 4:
            return False

        return True

    def perplexity(self):
        return math.pow(2.0, self.entropy())

    def entropy(self):
        h = 0.0
        for n, p in self.PR.items():
            h += p * math.log(p, 2.0)
        return -h

    def sort_by_pr(self):
        sort(self.PR)

    def sort_by_inlink(self):
        in_link_counts = dict()
        for k, v in self.graph.in_links.items():
            in_link_counts[k] = len(v)
        sort(in_link_counts)


def sort(dictionary):
    # sort dictionary descendingly by values
    sorted_nodes = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
    print_pages(sorted_nodes[:50])


def print_pages(nodes):
    for k, v in nodes:
        print(k + ":", v)