# -*- coding: utf-8 -*-
"""
Intro: web scraping
Ref: https://www.dataquest.io/blog/web-scraping-tutorial-python/

"""

import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page
page.status_code  # 200 means downloaded successfully, 4.* or 5.* means error

page.content

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())  # print HTML content


# finding 1 single line
list(soup.children)  # soup.children is a list iterator
[type(item) for item in list(soup.children)]
html = list(soup.children)[2]
list(html.children)
for i, child in enumerate(list(html.children)):
    print(i, child)
    
body = list(html.children)[3]
list(body.children)  # all content in index 1

p = list(body.children)[1]
p
p.get_text()


# finding all instances of a tag
soup.find_all('p')  # returns a list
soup.find_all('head')
soup.find_all('title')

soup.find_all('p')[0].get_text()  # use on single element of list
soup.find('p')  # finds first instance
