from selenium import webdriver
from lxml import etree
import time

browser = webdriver.Safari()
browser.implicitly_wait(10)
url = r"https://elearning.shanghaitech.edu.cn:8443/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1"
browser.get(url)
# print(browser.find_element_by_name("username"))
time.sleep(1)
browser.find_element_by_name("username").send_keys("2020533185")
time.sleep(1)
# print(browser.find_element_by_id("password"))
browser.find_element_by_id("password").send_keys("Quebec20071227")
time.sleep(1)
# print(browser.find_element_by_xpath("""//*[@id="casLoginForm"]/p[4]/button"""))
browser.find_element_by_xpath("""//*[@id="casLoginForm"]/p[4]/button""").click()
time.sleep(1)
source = browser.page_source
# print(source)
html = etree.fromstring(source)  # A fucking bug from nowhere
# html.xpath("""""")
print(html)
time.sleep(5)
browser.quit()

