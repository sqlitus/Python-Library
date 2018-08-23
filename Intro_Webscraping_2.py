'''
Tutorial: https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/

'''

### Part 1: Beautifulsoup Parsing ###

import bs4 as bs
import urllib.request
import re

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source, 'lxml')

print(soup.prettify())
soup.prettify()

# title of the page
print(soup.title)

# get attributes:
print(soup.title.name)

# get values:
print(soup.title.string)

# beginning navigation:
print(soup.title.parent.name)

# getting specific values:
print(soup.p)
print(soup.p.prettify())

# find all paragraphs
print(soup.find_all('p'))

# iterate through tags & print
for paragraph in soup.find_all('p'):
    print(paragraph.string)  # will return None if has child tags
    print(str(paragraph.text))

# get all links
for url in soup.find_all('a'):
    print(url.get('href'))

# just text
print(soup.get_text())



### Part 2: Navigating tags ###

# get the navigation bar
nav = soup.nav  # bs4.element.Tag
nav  # soup.find_all('nav')

# find all links in nav bar. double prints because of hidden mobile site's nav bar
for url in nav.find_all('a'):
    print(url.get('href'))  # string

# get body text
body = soup.body
body

# print all paragraphs in body
for paragraph in body.find_all('p'):
    print(paragraph.text)

# print just the div w/ class body
soup.find_all('div')  # lots of divs
soup.find_all('div', class_='body')  # wildcard match w/ class_ = "body"
for div in soup.find_all('div', class_='body'):
    print(div.text)









# Reference

soup.p
print(soup.p)
print(soup.p.prettify())
soup.a

soup.p  # finds first occurrence
soup.find_all('a')  # finds all
type(soup.find_all('a'))  # ResultSet
type(soup.p)  #Tag
