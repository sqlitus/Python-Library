### Get Call Data ###

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# !!!!!!!!!!!!!!!! set profile for automatically opening excel file
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.helperApps.neverAsk.openFile", True)

driver = webdriver.Firefox(firefox_profile=fp)
driver.get('https://10.2.89.122:8444/cuic/Main.htmx')   # .get() will automatically wait for page to load

login = driver.find_element_by_id('rawUserName')
login.send_keys('chris.jabr')  # f.l
login.send_keys(Keys.RETURN)

# wait for password field, then enter it
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'j_password')))
driver.find_element_by_id('j_password').send_keys('135790' + Keys.RETURN)  #tmlkps

# wait for navbar, then click reports
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Reports')))
reports_link = driver.find_elements_by_link_text('Reports')
reports_link[0].click()

### Switch to iframe to get reports (switch back out when done) ###
driver.switch_to.frame(driver.find_element_by_id("remote_iframe_4"))

# Navigate to report: Stock > Unified CCX Historical > Inbound > Contact Service Queue Activity Report
driver.find_element_by_xpath("//div[@class='ngCellText name_cell_container colt0']").click()
driver.find_element_by_xpath("//span[@class='ellipsis ng-binding'][@title='Unified CCX Historical']").click()
driver.find_element_by_xpath("//span[@class='ellipsis ng-binding'][@title='Inbound']").click()
driver.find_element_by_xpath("//span[@class='ellipsis ng-binding'][@title='Contact Service Queue Activity Report']").click()



# !!!!!!!!!!!!!!!!! Choose date: Click 'Date Range' dropdown. Click 'Yesterday'
'''
# only working after already clicked...
driver.find_element_by_xpath("//div[@class='csSelect-container ng-isolate-scope ng-valid ng-dirty ng-valid-parse']").click()
driver.find_element_by_xpath("//a[@class='ng-binding'][@title='Yesterday']").click()

### !!!!! above not working without first clicking... redo above...
driver.find_element_by_xpath("//a[@class='select-toggle form-control ng-binding ng-scope']").click()
driver.find_element_by_xpath("//i[@class='icon icon-chevron-down']").click()
driver.find_element_by_xpath("//div[@class='ng-scope dropdown']").click()
driver.find_element_by_xpath("//div[@class='select-list']").click()
driver.find_element_by_xpath("//div[@class='csSelect-container ng-isolate-scope ng-valid']").click()  # hmm..
driver.find_element_by_xpath("//select[@class='csSelect-container ng-isolate-scope ng-valid']").click()

driver.find_element_by_xpath("//div[@class='ng-scope dropdown']").click()
driver.find_element_by_xpath("//div[contains(text(), 'Today')]").click()
driver.find_element_by_xpath("//div[@class='csSelect-container ng-isolate-scope ng-valid ng-dirty ng-valid-parse']").click()
driver.find_element_by_xpath("//div[@class='editFilterPopup overflow_auto padding_20px display_flex bc_FFFFFF flex_column flex_1 overflow_hidden ng-scope']").click()
driver.execute_script("$(arguments[0]).click();", driver.find_element_by_xpath("//div[@class='ng-scope dropdown']"))
driver.execute_script("$(arguments[0]).click();", driver.find_element_by_xpath("//div[@class='ng-scope dropdown']"))

driver.find_element_by_xpath("//div[@class='csSelect-container ng-isolate-scope ng-valid']").send_keys(Keys.RETURN)
driver.find_element_by_xpath("//div[@class='csSelect-container ng-isolate-scope ng-valid']")
driver.find_element_by_xpath("//a[@class='select-toggle form-control ng-binding ng-scope']")
'''




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

# Export to excel: Click dropdown, click excel
driver.find_element_by_xpath("//div[@class='btn-group cuic-option-dropdown dropdown']").click()
driver.find_element_by_xpath("//a[@class='ng-binding'][@title='Export']").click()

# open the excel file dialog

### End
driver.close()




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