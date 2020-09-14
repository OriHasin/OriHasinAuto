from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver2=webdriver.Firefox \
    (executable_path="C:/Users/User/Desktop/Ori Selenium/geckodriver.exe")  # הגדרת אובייקט מסוג WebDriver ומשייך אליו את הדרייבר של הדפדפן
driver2.get("https://www.google.com/")                                      # שולח אותו לURL מוגדר

driver2.implicitly_wait(10)                                                 # זמן מוגבל של עד 10 שניות להמתנה שאלמנט יעלה - אחרת הפעולה תסגר

#sleep(2)                                                                   # השעייה של 2 שניות

#driver2.close()                                                            # סוגר את הפעולה של הדרייבר

driver2.maximize_window()                                                   # הגדלה של חלון התוכנית

#driver2.find_element_by_css_selector(".gLFyf").send_keys("מטרה")            # הפקודה הראשונה (find_element) מגדירה לתוכנית לחפש אלמנט מסוים בעמוד ולגשת אליו (במקרה הזה שורת החיפוש) , הפקודה השניה (send_keys) מגדירה לו אילו ערכים לשים באלמנט שמצאנו
#driver2.find_element_by_css_selector \
#    (".FPdoLc > center:nth-child(1) > input:nth-child(1)").click()          # הגדרנו לו למצוא אלמנט מסוים (כפתור החיפוש) ולאחר מכן ללחות עליו

text=driver2.find_element_by_css_selector("div.gb_h:nth-child(1) > a:nth-child(1)").text #השמת הטקסט שיש באלמנט מסויים לתוך משתנה (במקרה הזה לחצן הGmail)

print(text)
#driver2.find_element_by_css_selector(".gLFyf").send_keys("מטרה"+Keys.ENTER) #דרך שניה לחיפוש בדפדפן , על ידי ייבוא של לחצנים , נשלח אותו לאלמנט , נגדיר לו אילו ערכים לשים באלמנט ולאחר מכן שילחץ אנטר

driver2.find_element_by_css_selector(".gLFyf").send_keys("מטרה")
text_input=driver2.find_element_by_css_selector(".gLFyf").get_attribute("value") #משים את הערך שהמשתמש הכניס לתוך התיבת חיפוש לתוך משתנה כלומר את הערך "מטרה"

