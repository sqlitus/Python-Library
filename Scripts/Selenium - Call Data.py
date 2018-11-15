### Get Call Data ###

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
import os


# TODO: correctly set profile for automatically opening excel file
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.preferences.instantApply", True)
fp.set_preference("browser.download.manager.showWhenStarting", False)
# fp.set_preference("browser.helperApps.neverAsk.openFile", "application/vnd.ms-excel")  # this just selects the window option. doesn't automatically open it.
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel")

# set headless
opts = Options()
# opts.headless = True

driver = webdriver.Firefox(firefox_profile=fp, options=opts)
print("Firefox Headless Browser Invoked")
driver.get('https://10.2.89.122:8444/cuic/Main.htmx')   # .get() will automatically wait for page to load

login = driver.find_element_by_id('rawUserName')
login.send_keys('')  # f.l
login.send_keys(Keys.RETURN)

# wait for password field, then enter it
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'j_password')))
driver.find_element_by_id('j_password').send_keys('')  #tmlkps
driver.find_element_by_id('j_password').send_keys(Keys.RETURN)

# wait for navbar, then click reports
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, 'Reports')))
print("inside site. navigating to report.")
reports_link = driver.find_elements_by_link_text('Reports')
reports_link[0].click()

### Switch to iframe to get reports (switch back out when done) ###
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'remote_iframe_4')))
driver.switch_to.frame(driver.find_element_by_id("remote_iframe_4"))


### Xpath function
# def waitAndClick(xpath_string, webdriver_object):
#     WebDriverWait(webdriver_object, 20).until(EC.presence_of_element_located((By.XPATH, xpath_string)))
#     webdriver_object.execute_script("arguments[0].click();", webdriver_object.find_element_by_xpath(xpath_string))
#
# waitAndClick("//span[@class='ellipsis ng-binding'][@title='Stock']", driver)
# waitAndClick("//span[@class='ellipsis ng-binding'][@title='Unified CCX Historical']", driver)
# waitAndClick("//span[@class='ellipsis ng-binding'][@title='Inbound']", driver)
# waitAndClick("//span[@class='ellipsis ng-binding'][@title='Contact Service Queue Activity Report']", driver)

# Navigate to report: Stock > Unified CCX Historical > Inbound > Contact Service Queue Activity Report
WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, "//span[@class='ellipsis ng-binding'][@title='Stock']"))) #.click()
driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//span[@class='ellipsis ng-binding'][@title='Stock']"))
driver.find_element_by_xpath("//span[@class='ellipsis ng-binding'][@title='Unified CCX Historical']").click()
driver.find_element_by_xpath("//span[@class='ellipsis ng-binding'][@title='Inbound']").click()
driver.find_element_by_xpath("//span[@class='ellipsis ng-binding'][@title='Contact Service Queue Activity Report']").click()

# Wait, Find date dropdown. Click. Wait & Select Yesterday.
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='select-toggle form-control ng-binding ng-scope'][@title='Today']")))
print('selecting date parameters (yesterday).')
dropdown_date = driver.find_element_by_xpath("//a[@class='select-toggle form-control ng-binding ng-scope'][@title='Today']")
driver.execute_script("arguments[0].click();", dropdown_date)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='ng-binding'][@title='Yesterday']")))
driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//a[@class='ng-binding'][@title='Yesterday']"))

# Choose parameters: search OPOS, Click CSQ Names (@param4) & add to filters
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@class='cuic-switcher-search-field'][@title='Search Available']")))
print('selecting team parameters.')
driver.find_element_by_xpath("//input[@class='cuic-switcher-search-field'][@title='Search Available']").send_keys('opos')

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[@class='cuic-switcher-name ellipses ng-binding'][@title='OPOS_Aloha']")))
driver.find_element_by_xpath("//span[@class='cuic-switcher-name ellipses ng-binding'][@title='OPOS_Aloha']").click()
driver.find_element_by_xpath("//div[@class='icon cuicfont right']").click()
driver.find_element_by_xpath("//span[@class='cuic-switcher-name ellipses ng-binding'][@title='OPOS_NCR_Tech']").click()
driver.find_element_by_xpath("//div[@class='icon cuicfont right']").click()
driver.find_element_by_xpath("//span[@class='cuic-switcher-name ellipses ng-binding'][@title='OPOS_Payment']").click()
driver.find_element_by_xpath("//div[@class='icon cuicfont right']").click()
driver.find_element_by_xpath("//span[@class='cuic-switcher-name ellipses ng-binding'][@title='OPOS_R10']").click()
driver.find_element_by_xpath("//div[@class='icon cuicfont right']").click()

# Click 'Run' button
driver.find_element_by_xpath("//button[@class='bc_lightgreen finishButton ng-binding']").click()
print('running report')

# wait for table to load before exporting (helps for future navigation)
WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, "//td[@class='progressTD'][contains(text(), 'Success')]")))


# delete old file if exists
# try:
#     os.remove()
#     print('deleting old CSQAR file before download')
# except OSError:
#     print('no duplicate file. downloading normally')
#     pass

# Export to excel: Wait for page & visibility
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn dropdown-toggle']")))
dropdown_export = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn dropdown-toggle']")))
driver.execute_script("arguments[0].click();", dropdown_export)
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='ng-binding'][@title='Export']")))
driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//a[@class='ng-binding'][@title='Export']"))
print('exporting file.')

### End
time.sleep(3)
driver.quit()




### Reference

## go back
'''
driver.execute_script("window.history.go(-1)")
'''

## action chain isn't holding click on everything
'''
ActionChains(driver).key_down(Keys.CONTROL) \
    .click(driver.find_element_by_xpath("//span[@class='cuic-switcher-name ellipses ng-binding'][@title='OPOS_NCR_Tech']"))
    .click(driver.find_element_by_xpath("//span[@class='cuic-switcher-name ellipses ng-binding'][@title='OPOS_Payment']"))
    .click(driver.find_element_by_xpath("//span[@class='cuic-switcher-name ellipses ng-binding'][@title='OPOS_R10']"))
    .key_up(Keys.CONTROL)
    .perform()
'''

## custom wait & method function (unfinished)
'''
def wait_and_click(driver, xpath):
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
    ele = driver.find_element_by_xpath(xpath)
    driver.execute_script("arguments[0].click();", ele)
'''