from bs4 import BeautifulSoup
import urllib
import urllib.request


def scrape(url, element):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    scrapedElement = soup.element
    return scrapedElement
