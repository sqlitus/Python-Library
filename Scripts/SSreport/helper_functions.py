# using chrome

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


### Browser wait & click behavior Xpath function
def waitAndAct(xpath_string, browser, action, wait=20):

    WebDriverWait(browser, wait).until(EC.visibility_of_element_located((By.XPATH, xpath_string)))
    xpath_element = browser.find_element_by_xpath(xpath_string)

    if action == 'click':
        browser.execute_script("arguments[0].click();", xpath_element)
    elif action == 'hover':
        ActionChains(browser).move_to_element(xpath_element).perform()
    elif action == 'right click':
        ActionChains(browser).context_click(xpath_element).perform()


### Export report function
def export_report(browser):

    # right click menu -> download excel
    waitAndAct("//th[@name='number']", browser, 'right click')  # opens menu
    waitAndAct("//div[@item_id='d1ad2f010a0a0b3e005c8b7fbd7c4e28']", browser, 'hover')  # hover over export
    waitAndAct("//div[@item_id='f13f0041473012003db6d7527c9a71f0']", browser, 'hover')  # in '>' menu, hover over Excel
    waitAndAct("//div[@item_id='f13f0041473012003db6d7527c9a71f0']", browser, 'click')  # click Excel


### Download report function
def download_report(browser, wait=20):
    # wait for 'export_complete' sign, and download
    WebDriverWait(browser, wait).until(EC.visibility_of_element_located((By.XPATH, "//tr[@id='export_complete']")))
    waitAndAct("//button[@id='download_button']", browser, 'click')  # click in-browser download


### List full file paths for all files in directory function
def listdir_full_path(path):
    return [os.path.join(path, f) for f in os.listdir(path)]



