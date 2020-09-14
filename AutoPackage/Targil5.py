from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome(executable_path="C:/Users/User/Desktop/Ori Selenium/chromedriver.exe")
driver.get("https://juliemr.github.io/protractor-demo/")
driver.find_element_by_css_selector("input[ng-model='first']").send_keys("4")
select=Select(driver.find_element_by_css_selector("select[ng-model='operator']"))
select.select_by_visible_text('*')
driver.find_element_by_xpath("//input[@ng-model='second']").send_keys("4")
driver.find_element_by_xpath("//button[@ng-click='doAddition()']").click()
element=driver.find_element_by_tag_name("h2")
#WebDriverWait(driver,2).until((EC.visibility_of_element_located(By.TAG_NAME,'h2')))
while('.' == element.text[0]):
    print(element.text)
    continue
if element.text==str(16):
    print("Success")
else:
    print("Not Success")