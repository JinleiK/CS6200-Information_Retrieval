#!/usr/bin/python python
# -*- coding: utf-8 -*-

__author__ = 'callie'

import urlparse
import urllib
import time
import sys
from bs4 import BeautifulSoup

# Global Variables
MAX_DEPTH = 3
URL_HEAD = "http:"
DOMAIN = "http://en.wikipedia.org"
PREFIX = "http://en.wikipedia.org/wiki/"
MAINPAGE = "http://en.wikipedia.org/wiki/main_page"
urls = []  # to store the valid urls to crawl
visited = {}  # to store the valid visited urls


def crawler(seed, key):
    depth = 1
    urls.append(depth)
    urls.append(seed)

    while len(urls) > 0:
        maybe_url = urls.pop(0)
        if str(maybe_url)[:1] != "h":
            depth = maybe_url
            maybe_url = urls.pop(0)

        url = maybe_url
        try:  # open the URL and get the page source
            html_text = urllib.urlopen(url).read()
        except urllib.IOError:  # if fail to open, stop
            print("cannot open " + url)
            continue
        if key not in html_text.lower():
            continue
        soup = BeautifulSoup(html_text)
        title = soup.title.string
        if title not in visited:
            visited[title] = url
            print(url, depth)
        if depth < MAX_DEPTH:
            urls.append(depth + 1)
            for tag in soup.findAll('a', href=True):
                link = tag['href']
                pos = link.find("#")
                if pos > 0:
                    link = link[:pos]
                if link.startswith("//"):
                    link = urlparse.urljoin(URL_HEAD, link)
                # print("//:" + link)
                elif link.startswith("/"):  # if the URL is relative, join it with its domain
                    link = urlparse.urljoin(DOMAIN, link)
                link_rest = link[6:]
                if ":" not in link_rest and PREFIX in link and link != MAINPAGE:
                    urls.append(link)


if __name__ == '__main__':
    start_time = time.time()
    if len(sys.argv) == 3:
        seed_page = sys.argv[1]
        key_phrase = sys.argv[2]
        crawler(seed_page, key_phrase)
    elif len(sys.argv) == 2:
        seed_page = sys.argv[1]
        crawler(seed_page, "")
    else:
        print("Usage: seedPage [keyphrase]")
    print("---------------------")
    for k, v in visited.items():
        print(v)
    print(time.time() - start_time)