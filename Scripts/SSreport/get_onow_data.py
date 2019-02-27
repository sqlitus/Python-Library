### Get onow Data ###

# Purpose: automate web navigation & extraction of data from several reports


import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
print('cwd:', os.getcwd())


# custom modules
from Scripts.SSreport.helper_functions import *  # navigation functions
from Scripts.SSreport import creds  # get creds



#### Selenium Navigation ####


### Instantiate driver w/ download options
ss_download_path = os.path.join(os.getenv('USERPROFILE'), r'Downloads\Snapshot Report Data')
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory": ss_download_path}
chromeOptions.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(executable_path=os.path.join(os.getcwd(), r'Resources\chromedriver.exe'), chrome_options=chromeOptions)  # , chrome_options=chromeOptions


### Get into site
browser.get('http://wfmprod.service-now.com/')
WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='loginfmt']")))
li = browser.find_element_by_xpath("//input[@name='loginfmt']")
li.send_keys(creds.creds['li'])
li.send_keys(Keys.RETURN)

time.sleep(1)
WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='passwd']")))
pw = browser.find_element_by_xpath("//input[@name='passwd']")
pw.send_keys(creds.creds['pw'])
waitAndAct("//input[@type='submit']", browser, 'click')


### Wait for site entrance; Open all reports in tabs. Tabs open as 0=first, 1=right-most, 2=2nd from right, etc
WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='navbar-brand']")))
browser.get(creds.creds['ss_rs_i']); time.sleep(1)
browser.execute_script("window.open('" + creds.creds['ss_ghd_i'] + "')"); time.sleep(1)
browser.execute_script("window.open('" + creds.creds['ss_ghd_sc_t'] + "')")


### Export report from each tab
# TODO: tabs are out of order (1,3,2). go in creation order...
for i, tab in enumerate(browser.window_handles):
    print('tab index', i, '.', tab)
    browser.switch_to.window(tab)
    export_report(browser)
    print(f'exporting report tab {i}: {browser.title}')
    time.sleep(1)


### Before download: delete old files in destination folder if they exist
try:
    for file in listdir_full_path(ss_download_path):
        os.remove(file)
        print('Old files found. Deleting:', file)
except OSError:
    print('Empty directory:', ss_download_path, '\nDownloading files.')
    pass


### Download each report
for i, tab in enumerate(browser.window_handles):
    browser.switch_to.window(tab)
    download_report(browser)
    print(f'downloading report tab {i}: {browser.title}')
    time.sleep(1)






#### Test ####

# browser_tabs = []
# browser_tabs.append(browser.current_window_handle)
#
#
#
# browser.current_window_handle
# browser.window_handles
# browser.window_handles[2]
# browser.switch_to.window(browser.window_handles[2])
#
# for i, tab in enumerate(browser.window_handles):
#     browser.switch_to.window(tab)
#     print(f'window {i} has title {browser.title}')
#     time.sleep(2)


# creds.creds[0]
# creds.creds
# list(creds.creds)[0]
#
#
#
#
# browser.window_handles
# browser.current_window_handle
# browser.current_window_handle in browser.window_handles
# browser.window_handles[1]
# browser.window_handles[browser.window_handles == browser.current_window_handle]
# browser.switch_to.window(browser.window_handles[0])
#
# for i in range(len(browser.window_handles)):
#     if browser.window_handles[i] == browser.current_window_handle:
#         print('current browser is at index', i, ' out of 0 - ', len(browser.window_handles)-1)
#
#
#
#
# browser.close()



# TODO: confirm file creation date & inside data is aligned w/ report
# TODO: Rename file? Scan files for correct data
# TODO: IMPORT PANDAS + ANALYZE
# TODO: FORMAT, PUT IN OUTLOOK EMAIL