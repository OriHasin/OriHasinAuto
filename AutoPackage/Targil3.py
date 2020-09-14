from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
driver=webdriver.Chrome(executable_path="C:/Users/User/Desktop/Ori Selenium/chromedriver.exe")
driver.get("https://www.phptravels.net/admin")
driver.maximize_window()
driver.find_element_by_xpath("//input[@type='text'][1]").send_keys("admin@phptravels.com")
driver.find_element_by_css_selector("input[name=password]").send_keys("demoadmin")
driver.find_element_by_class_name("ladda-label").click()
sleep(4)
driver.find_element_by_css_selector("button[data-toggle='modal']").click()
#driver.find_element_by_css_selector("ul>li>a[href='https://www.phptravels.net/admin']").click()
element = driver.find_element_by_xpath("//select[@name='applytax']")
sleep(2)
Select1=Select(element)
Select1.select_by_visible_text('Yes')
element2 = driver.find_element_by_id("servicetype")
Select2=Select(element2)
Select2.select_by_visible_text('Hotels')
driver.find_element_by_css_selector("button[class='btn btn-primary']").click()


