__author__ = 'callie'

import sys
from PageGraph import PageGraph
from PageRank import PageRank


def small_graph(file_path):
    graph = PageGraph(file_path)
    graph.fetch_graph()
    page_ranker = PageRank(graph)
    page_ranker.rank("small")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        f = sys.argv[1]
        small_graph(f)
    else:
        print "Usage: filePath"