#-*- coding:utf-8 -*- 
#RF:<phantomjs和selenium设置proxy、headers> http://blog.csdn.net/tcorpion/article/details/70213435

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
from bs4 import BeautifulSoup


desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
desired_capabilities["phantomjs.page.settings.userAgent"] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'

driver = webdriver.PhantomJS(service_args=[], executable_path='/usr/bin/phantomjs', desired_capabilities=desired_capabilities)
driver.set_page_load_timeout(20)
driver.set_script_timeout(20)

driver.get('http://www.baidu.com')
driver.implicitly_wait(10)
search_txt = driver.find_element_by_xpath("//*[@id='kw']") #? how to set value
driver.execute_script('document.getElementById("kw").value="123"') #: use this way to set value
print "search text: %s" % search_txt.get_property("value")
search_btn = driver.find_element_by_xpath("//*[@id='su']")
search_btn.click()
#driver.execute_script('document.getElementById("su").click()') #: another way to do click

print "Check result..."
#driver.implicitly_wait(20) #:! not work here, have to use time.sleep() instead
import time; time.sleep(1)
print "Found................:" + str(driver.page_source.find("Boom") >= 0)
driver.save_screenshot('/home/tanjl/tmp/example.png')

soup = BeautifulSoup(driver.page_source, "html.parser")
#print soup.prettify().encode('utf8')

# quit() to avoid process remained background: /usr/bin/phantomjs --cookies-file=/tmp/tmpY2P1Mz --webdriver=54563
driver.quit()
