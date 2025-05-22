from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(0.5)

#launch URL
driver.get("https://the-internet.herokuapp.com/jqueryui/menu#")

#object of ActionChains
a = ActionChains(driver)

#identify element
m= driver.find_element(by=By.LINK_TEXT, value="Enabled")
#hover over element

a.move_to_element(m).perform()

#identify sub menu element
n= driver.find_element(by=By.LINK_TEXT, value="Back to JQuery UI")
# hover over element and click
a.move_to_element(n).click().perform()

print("Page title: " + driver.title)

#close browser
#driver.close()