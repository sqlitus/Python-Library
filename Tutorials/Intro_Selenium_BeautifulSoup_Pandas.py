# Navigate w/ Selenium
# Scrape w/ BeautifulSoup
# Structure w/ Pandas

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import numpy as np


opts = Options()
opts.headless = True    # invisible browser option
assert opts.headless
browser = Firefox(options=opts)
print("Firefox Headless Browser Invoked")
browser.get('https://duckduckgo.com')

search_form = browser.find_element_by_id('search_form_input_homepage')
search_form.send_keys('real python')
search_form.submit()

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'result')))  # my wait works
results = browser.find_elements_by_class_name('result')
print(results[0].text)




### scraping data - hand over to soup & turn into dataframe
from bs4 import BeautifulSoup as bs
import re

soup = bs(browser.page_source, 'html.parser')  # done with browser now
browser.quit()
print("Firefox Headless Browser CLOSED")

myresults = soup.find_all(class_='result')
result_list = []
for i in myresults:
    print(i.get_text())
    result_list.append(i.get_text())

df = pd.DataFrame({'result': result_list})


# Online example: https://realpython.com/modern-web-automation-with-python-and-selenium/
# resource: https://medium.freecodecamp.org/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251