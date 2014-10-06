__author__ = 'callie'

import sys
from PageGraph import PageGraph
from PageRank import PageRank


def big_graph(file_path):
    graph = PageGraph(file_path)
    graph.fetch_graph()
    # graph.test_graph()
    page_ranker = PageRank(graph)
    page_ranker.rank("big")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        f = sys.argv[1]
        big_graph(f)
    else:
        print "Usage: filePath"