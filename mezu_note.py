from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class IfReady:
    key = None

    @classmethod
    def ready(cls, driver):
        key = driver.find_element_by_class_name('wrap_edit').get_attribute('id')
        if key != cls.key:
            cls.key = key
            return True
        else:
            return False


url = "https://cloud.flyme.cn/browser/note.jsp"

driver = webdriver.Chrome()
driver.get(url)

input("continue")

item = driver.find_element_by_class_name('gpItemFocus')
items = driver.find_elements_by_class_name('groupItem')
print len(items)

for i, item in enumerate(items):
    item.click()
    WebDriverWait(driver, 60).until(IfReady.ready)
    date = driver.find_element_by_id("time").text
    memo = driver.find_element_by_id('dialogContent').text
    print date
    print memo
    print "----------\n"



#driver.execute_script("document.getElementByClass('wy-menu').scrollDown += 100");


