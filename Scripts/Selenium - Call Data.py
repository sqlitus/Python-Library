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
opts.headless = True

driver = webdriver.Firefox(firefox_profile=fp, options=opts)
print("**Firefox Headless Browser Invoked**")
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
print("logged in successfully. navigating to report.")
reports_link = driver.find_elements_by_link_text('Reports')
reports_link[0].click()

### Switch to iframe to get reports (switch back out when done) ###
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'remote_iframe_4')))
driver.switch_to.frame(driver.find_element_by_id("remote_iframe_4"))


### Xpath function
def waitAndClick(xpath_string, webdriver_object):
    WebDriverWait(webdriver_object, 20).until(EC.presence_of_element_located((By.XPATH, xpath_string)))
    webdriver_object.execute_script("arguments[0].click();", webdriver_object.find_element_by_xpath(xpath_string))


# Navigate to report: Stock > Unified CCX Historical > Inbound > Contact Service Queue Activity Report
waitAndClick("//span[@class='ellipsis ng-binding'][@title='Stock']", driver)
waitAndClick("//span[@class='ellipsis ng-binding'][@title='Unified CCX Historical']", driver)
waitAndClick("//span[@class='ellipsis ng-binding'][@title='Inbound']", driver)
waitAndClick("//span[@class='ellipsis ng-binding'][@title='Contact Service Queue Activity Report']", driver)

# Wait, Find date dropdown. Click. Wait & Select Yesterday.
waitAndClick("//a[@class='select-toggle form-control ng-binding ng-scope'][@title='Today']", driver)
print('selecting date parameters (yesterday).')
waitAndClick("//a[@class='ng-binding'][@title='Yesterday']", driver)

# Choose parameters: search OPOS, then Click CSQ Names (@param4) & add to filters
waitAndClick("//input[@class='cuic-switcher-search-field'][@title='Search Available']", driver)
print('selecting team parameters.')
driver.find_element_by_xpath("//input[@class='cuic-switcher-search-field'][@title='Search Available']").send_keys('opos')

waitAndClick("//span[@class='cuic-switcher-name ellipses ng-binding'][@title='OPOS_Aloha']", driver)
waitAndClick("//div[@class='icon cuicfont right']", driver)  # click right arrow
waitAndClick("//span[@class='cuic-switcher-name ellipses ng-binding'][@title='OPOS_NCR_Tech']", driver)
waitAndClick("//div[@class='icon cuicfont right']", driver)  # click right arrow
waitAndClick("//span[@class='cuic-switcher-name ellipses ng-binding'][@title='OPOS_Payment']", driver)
waitAndClick("//div[@class='icon cuicfont right']", driver)  # click right arrow
waitAndClick("//span[@class='cuic-switcher-name ellipses ng-binding'][@title='OPOS_R10']", driver)
waitAndClick("//div[@class='icon cuicfont right']", driver)  # click right arrow

# Click 'Run' button
waitAndClick("//button[@class='bc_lightgreen finishButton ng-binding']", driver)
print('running report')

# wait for table to load before exporting (helps for future navigation)
WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, "//td[@class='progressTD'][contains(text(), 'Success')]")))

# delete old file if exists
CSQAR_filename = r"Contact Service Queue Activity Report-Contact Service Queue Activity Report.xls"
CSQAR_full_path = os.path.join(os.getenv('USERPROFILE'), 'Downloads', CSQAR_filename)

try:
    os.remove(CSQAR_full_path)
    print('deleting old CSQAR file before download')
except OSError:
    print('no duplicate file. downloading normally')
    pass

# Export table to excel: Wait for page & visibility
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn dropdown-toggle']")))
dropdown_export = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn dropdown-toggle']")))
driver.execute_script("arguments[0].click();", dropdown_export)
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='ng-binding'][@title='Export']")))
driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//a[@class='ng-binding'][@title='Export']"))
print('exporting file.')

# wait & check if downloaded successfully
for i in range(15):
    if not os.path.exists(CSQAR_full_path):
        time.sleep(1)
        print('waiting on file download to complete.')
    else:
        print('download completed in', os.path.join(os.getenv('USERPROFILE'), 'Downloads'))
        break
else:
    print('download not found after 15 seconds.')

### End
driver.quit()
