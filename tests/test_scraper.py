from bs4 import BeautifulSoup
from scraper import *
import urllib
import urllib.request
import pytest


url = "https://www.google.com"
thepage = urllib.request.urlopen(url)
soup = BeautifulSoup(thepage, "html.parser")

print(soup.title)


def test_scraper_get_element():
    url = "https://www.google.com"
    element = "title"
    assert scrape(url, element) == "<title>Google</title>"
