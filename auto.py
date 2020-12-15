from selenium import webdriver

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


chrome_path= r"D:\auto\chromedriver.exe"
browser = webdriver.Chrome(chrome_path)
browser.get('http://www.my-gurukul.com/login.aspx?BROWSERWINDOW=&BROWSER=FF&DF=MM/DD/YYYY&CF=MYGURUKUL&SID=1022')

mail=browser.find_element_by_xpath('//*[@id="txtUserName"]')
mail.send_keys("1NT15IS123")
               
passw=browser.find_element_by_xpath('//*[@id="txtPassword"]')
passw.send_keys("XXX12345")

butt=browser.find_element_by_xpath('//*[@id="Validate"]')
butt.click()

browser.implicitly_wait(10)

browser.find_element_by_xpath('//a[img/@src="images/lbxclose.jpeg"]').click()


try:
    myElem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'imgid_22')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

time.sleep(4)
browser.refresh()

#browser.implicitly_wait(10)
#att=browser.find_element_by_xpath('//*[@id="imgid_12"]')
#att.click()