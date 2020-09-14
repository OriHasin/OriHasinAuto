from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:/Users/User/Desktop/Ori Selenium/chromedriver.exe")
driver.get("https://www.phptravels.net/admin")
driver.maximize_window()
driver.find_element_by_xpath("//input[@type='text'][1]").send_keys("admin@phptravels.com")
driver.find_element_by_css_selector("input[name=password]").send_keys("demoadmin")
driver.find_element_by_class_name("ladda-label").click()
sleep(8)
text=driver.find_element_by_css_selector("ul>li>a[href='https://www.phptravels.net/admin']").text
if text == 'DASHBOARD':
    print("Succes")
else:
    print("Good Job Ori")
#driver.find_element_by_xpath("//li/a/strong/i").click()










