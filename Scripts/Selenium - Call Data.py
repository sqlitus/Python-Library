### Get Call Data ###

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://10.2.89.122:8444/cuic/Main.htmx')   # .get() will automatically wait for page to load

login = driver.find_element_by_id('rawUserName')
login.send_keys('')  # f.l
login.send_keys(Keys.RETURN)

login_2 = driver.find_element_by_id('j_password')
login_2.send_keys('')  # tmlkps
login_2.send_keys(Keys.RETURN)

# need to wait to load...
reports_link = driver.find_elements_by_link_text('Reports')
reports_link[0].click()








# ******************* go to stock report. none of these work.
driver.find_elements_by_link_text('Reports')[0].text
driver.find_elements_by_link_text('Reports')
driver.find_element_by_class_name("colt0")

driver.find_element_by_xpath("//div[@class='ngCellText name_cell_container colt0'")
driver.find_element_by_xpath("//div[@class='ng-scope ngRow even ui-state-default'")
driver.find_element_by_xpath("//div[@class='ngCell  col0 colt0'")
driver.find_element_by_xpath("//div[@class='ngCell/col0/colt0'")

driver.find_element_by_class_name('icon icon-folder ng-scope')
driver.find_element_by_class_name('nameCell')

driver.find_element_by_css_selector('div ng-cell')
driver.find_element_by_css_selector('div + ng-scope ngRow even ui-state-default')

driver.find_element_by_css_selector("//div")


# fill in report params
# run
# export










driver.close()

### Reference
## go back
# driver.execute_script("window.history.go(-1)")

