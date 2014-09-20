__author__ = 'callie'

#!/usr/bin/python python
# -*- coding: UTF-8 -*-
import urlparse
import urllib
import time
import sys
from bs4 import BeautifulSoup

maxDepth = 3
urlhead = "http:"
prefix = "http://en.wikipedia.org/wiki/"
mainpage = "http://en.wikipedia.org/wiki/main_page"
visited = []


def crawler(url, key, depth):
    url_rest = url[6:]
    if ":" in url_rest:
        return
    try:
        htmltext = urllib.urlopen(url).read()
    except:
        print("cannot open " + url, depth)
        return
    if key not in htmltext:
        return
    print(url, depth)
    visited.append(url)
    soup = BeautifulSoup(htmltext)
    if depth > 1:
        for tag in soup.findAll('a', href=True):
            link = tag['href'].lower()
            if link.startswith("//"):
                link = urlparse.urljoin(urlhead, link)
            if link.startswith("/"):
                parsed_url = urlparse.urlparse(url)
                domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_url)
                link = urlparse.urljoin(domain, link)

            if link not in visited and prefix in link and link != mainpage:
                # print(link)
                # time.sleep(1)
                crawler(link, key, depth - 1)
                # print("yeah")


if __name__ == '__main__':
    start_time = time.time()
    if len(sys.argv) == 3:
        seedPage = sys.argv[1]
        keyphrase = sys.argv[2]
        crawler(seedPage, keyphrase, maxDepth)
    elif len(sys.argv) == 2:
        seedPage = sys.argv[1]
        crawler(seedPage, "", maxDepth)
    else:
        print("Usage: seedPage [keyphrase]")

    print("----------------------")
    for v in visited:
        print(v)
    print(time.time() - start_time)