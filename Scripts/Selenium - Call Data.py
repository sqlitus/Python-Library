### Get Call Data ###

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# TODO: correctly set profile for automatically opening excel file
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.preferences.instantApply", True)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.helperApps.neverAsk.openFile", "text/plain, text/csv, application/csv, application/excel")

driver = webdriver.Firefox(firefox_profile=fp)
driver.get('https://10.2.89.122:8444/cuic/Main.htmx')   # .get() will automatically wait for page to load

login = driver.find_element_by_id('rawUserName')
login.send_keys('')  # f.l
login.send_keys(Keys.RETURN)

# wait for password field, then enter it
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'j_password')))
driver.find_element_by_id('j_password').send_keys('')  #tmlkps
driver.find_element_by_id('j_password').send_keys(Keys.RETURN)

# wait for navbar, then click reports
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Reports')))
reports_link = driver.find_elements_by_link_text('Reports')
reports_link[0].click()

### Switch to iframe to get reports (switch back out when done) ###
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'remote_iframe_4')))
driver.switch_to.frame(driver.find_element_by_id("remote_iframe_4"))

# Navigate to report: Stock > Unified CCX Historical > Inbound > Contact Service Queue Activity Report
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//span[@class='ellipsis ng-binding'][@title='Stock']"))) #.click()
driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//span[@class='ellipsis ng-binding'][@title='Stock']"))
driver.find_element_by_xpath("//span[@class='ellipsis ng-binding'][@title='Unified CCX Historical']").click()
driver.find_element_by_xpath("//span[@class='ellipsis ng-binding'][@title='Inbound']").click()
driver.find_element_by_xpath("//span[@class='ellipsis ng-binding'][@title='Contact Service Queue Activity Report']").click()

# Wait, Find date dropdown. Click. Wait & Select Yesterday.
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='select-toggle form-control ng-binding ng-scope'][@title='Today']")))
dropdown_date = driver.find_element_by_xpath("//a[@class='select-toggle form-control ng-binding ng-scope'][@title='Today']")
driver.execute_script("arguments[0].click();", dropdown_date)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='ng-binding'][@title='Yesterday']")))
driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//a[@class='ng-binding'][@title='Yesterday']"))

# Choose parameters: Click CSQ Names (@param4) & add to filters
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

# Export to excel: Wait & Click dropdown, Wait & click excel
# TODO: click even when minimized. regular .click() not working on minimzed window. execute_script not working either.
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='btn-group cuic-option-dropdown dropdown']")))
driver.find_element_by_xpath("//div[@class='btn-group cuic-option-dropdown dropdown']").click()
# driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//div[@class='btn-group cuic-option-dropdown dropdown']"))
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='ng-binding'][@title='Export']"))).click()
# driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//a[@class='ng-binding'][@title='Export']"))

# todo: auto open excel file
# click ok..? auto ok...?

### End
# driver.quit()




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

## custom wait & method function
'''
def wait_and_click(driver, xpath):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    ele = driver.find_element_by_xpath(xpath)
    driver.execute_script("arguments[0].click();", ele)
'''