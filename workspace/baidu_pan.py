#-*- coding:utf-8 -*- 

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
from bs4 import BeautifulSoup


desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
desired_capabilities["phantomjs.page.settings.userAgent"] = 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16'

from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get('http://pan.baidu.com')

for i,e in enumerate(driver.find_elements_by_xpath("//a")):
    print "%d...%s" % (i, e.text)
driver.find_elements_by_xpath("//a")[21].click()


driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_4__userName']").send_keys('june.tan@163.com')
driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_4__password']").send_keys(sys.argv[1])
driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_4__submit']").click()
driver.save_screenshot('/home/tanjl/tmp/example.png')


from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get('https://passport.baidu.com/v2/?login')
import time;time.sleep(5)
driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_3__userName']").send_keys('june.tan@163.com')
import time;time.sleep(2)
driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_3__password']").send_keys(sys.argv[1])
import time;time.sleep(2)
driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_3__submit']").click()
import time;time.sleep(3)
driver.save_screenshot('/home/tanjl/tmp/example.png')





from selenium.webdriver.common.keys import Keys
driver.send_keys(Keys.CONTROL + 'T')





from selenium import webdriver

driver2 = webdriver.PhantomJS()
driver.get('http://stackoverflow.com/')

cookies = driver.get_cookies()

driver.delete_all_cookies()

for cookie in cookies :
    driver.add_cookie({k: cookie[k] for k in ('name', 'value', 'domain', 'path', 'expiry')})


for cookie in driver.get_cookies():
    driver2.add_cookie({k: cookie[k] for k in ('name', 'value', 'domain', 'path')})

# quit() to avoid process remained background: /usr/bin/phantomjs --cookies-file=/tmp/tmpY2P1Mz --webdriver=54563
driver.quit()
