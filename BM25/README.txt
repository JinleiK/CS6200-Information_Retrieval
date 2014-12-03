==File structure==
report.pdf - answers for questions, implementation description
Indexer.py - python code for converting the corpus to inverted index lists
DocStatistics.py - DocStatistics class which fetches and stores the inverted index lists and needed statistics of the documents for calculating BM25 scores
BM25.py - BM25 class which calculates BM25 scores for one query
RunBM25.py - python code for reading queries and calculating BM25 scores for each query and output the required number of scores
tccorpus.txt - corpus file, input file for Indexer
queries.txt - queries file, input file for RunBM25
index.out - inverted index lists, output file of Indexer, input file for RunBM25
results.eval - documents' scores for each query with the rankings

==Instructions to run the code==

Requirements: 
you must have Python 3.0 or later version installed in your machine

There are several ways to run the code, below are two of them:
1. Open the code in a Python IDE, add parameters to Run Configurations, and then click the Run button. When completed, copy the console output to an empty file, e.g. output.txt
2. Or you can use python3 command in the command line in this folder
	1) for the small inverted indexer: python3 Indexer.py tccorpus.txt index.out
	2) for the BM25 ranker: python3 RunBM25.py index.out queries.txt <number> > results.eval
