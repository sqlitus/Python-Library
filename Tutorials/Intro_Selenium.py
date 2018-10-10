# reference (has degraded commands): https://realpython.com/modern-web-automation-with-python-and-selenium/

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

## open browser go to website
opts = Options()
# opts.headless = True
browser = Firefox(options=opts)
browser.get('https://bandcamp.com')
browser.find_element_by_class_name('play-btn').click()

## pick a dicover track
tracks = browser.find_elements_by_class_name('discover-item')  # contains string
len(tracks)  # 8
tracks[3].click()

## click next to scroll through options
next_button = browser.find_element_by_xpath("//a[@class='item-page'][contains(text(), 'next')]")

