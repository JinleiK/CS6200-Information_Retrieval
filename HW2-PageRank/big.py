__author__ = 'callie'

import sys
from PageGraph import PageGraph
from PageRank import PageRank


def big_graph(file_path):
    graph = PageGraph(file_path)
    graph.fetch_graph()
    page_ranker = PageRank(graph)
    page_ranker.rank("big")
    print("Top 50 pages sorted by PageRank:")
    page_ranker.sort_by_pr()
    print("Top 50 pages sorted by in-link count:")
    page_ranker.sort_by_inlink()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        f = sys.argv[1]
        big_graph(f)
    else:
        print ("Usage: PageRank <filePath>")