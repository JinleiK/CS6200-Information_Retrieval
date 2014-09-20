__author__ = 'callie'

#!/usr/bin/python python
# -*- coding: UTF-8 -*-
import urlparse
import urllib
import time
import sys
from bs4 import BeautifulSoup

# Global Variables
MAX_DEPTH = 3
URL_HEAD = "http:"
PREFIX = "http://en.wikipedia.org/wiki/"
MAINPAGE = "http://en.wikipedia.org/wiki/main_page"
visited = []  # store the valid visited urls


def crawler(url, key, depth_to_go):
    url_rest = url[6:]
    if ":" in url_rest:  # rule out the URL with a colon in the rest of it
        return
    try:  # open the URL and get the page source
        html_text = urllib.urlopen(url).read()
    except urllib.IOError:  # if fail to open, stop
        print("cannot open " + url)
        return
    if key not in html_text:  # rule out the URL without the key phrase
        return
    visited.append(url.lower())  # add the valid URL to the visited list
    soup = BeautifulSoup(html_text)
    if depth_to_go > 1:
        for tag in soup.findAll('a', href=True):  # find all the URLs in current page
            link = tag['href'].lower()
            if link.startswith("//"):
                link = urlparse.urljoin(URL_HEAD, link)
            if link.startswith("/"):  # if the URL is relative, join it with its domain
                parsed_url = urlparse.urlparse(url)
                domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_url)
                link = urlparse.urljoin(domain, link)
            # if the URL is not visited and has the required prefix but is not the main page,
            # craw the URL
            if link not in visited and PREFIX in link and link != MAINPAGE:
                time.sleep(1)  # delay one second between requests to the web server
                crawler(link, key, depth_to_go - 1)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        seed_page = sys.argv[1]
        key_phrase = sys.argv[2]
        crawler(seed_page, key_phrase, MAX_DEPTH)
    elif len(sys.argv) == 2:
        seed_page = sys.argv[1]
        crawler(seed_page, "", MAX_DEPTH)
    else:
        print("Usage: seedPage [keyphrase]")

    for v in visited:
        print(v)