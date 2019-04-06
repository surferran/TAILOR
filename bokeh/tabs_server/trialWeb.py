'''
from https://www.tocode.co.il/blog/2019-02-rotter-headlines-python?fbclid=IwAR3FSCPNXlJnStQlY74_21zEOCpjNepwX76X-TnB11ohnR0f75x6WRDZt_w
'''
import requests
from bs4 import BeautifulSoup
from lxml.html.soupparser import fromstring
from lxml import etree

url = 'http://rotter.net/'
r = requests.get(url)
r.encoding = 'iso8859-8'
root = fromstring(r.text)
headlines = [
        text for text in root.xpath('//a[@target="news"]/../text()')
        if text != '\n' and text != '\n\n' and text != '\xa0 '
]

for text in headlines:
    print(text)