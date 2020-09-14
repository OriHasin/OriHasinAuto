from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep
class HomePage:
    def __init__(self,driver):
        self.driver=driver
    def HeadPhonesCategory(self):
        return self.driver.find_element_by_id("headphonesImg")
    def TabletsCategory(self):
        return self.driver.find_element_by_id("tabletsImg")
    def LaptopsCategory(self):
        return self.driver.find_element_by_id("laptopsImg")
    def SpeakersCategory(self):
        return self.driver.find_element_by_id("speakersImg")
    def MiceCategory(self):
        return self.driver.find_element_by_id("miceImg")


