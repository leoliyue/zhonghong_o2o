
from selenium import webdriver
from selenium.webdriver.support.select import Select


class A:
    def __init__(self,a):
        self.a = a
    def add(self):
        return None
import time

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()

    driver.get('http://127.0.0.1:8000/Fangfull/contenturl/')
    time.sleep(3)
    click_newsUrl = driver.find_element_by_class_name('news_url')
    click_newsUrl.click()

    urlblue = driver.find_element_by_id('url_blue')
    urlblue.send_keys('http://test1www.xqshijie.com/')

    urlred = driver.find_element_by_id('url_red')
    urlred.send_keys('http://test2www.xqshijie.com/')

    urltype = driver.find_element_by_name('url_type')
    urltype.send_keys('1')



    # urlstuts = driver.find_element_by_xpath('//div/select[@name="url_stuts"]')
    # Select(urlstuts).select_by_value("1")

    sqlid = driver.find_element_by_xpath('//option[contains(text(),"房否测试站")]')
    sqlid.click()

    save = driver.find_element_by_tag_name('button').click()

    alert = driver.switch_to_alert()

    # alert.accept()#确认
    # alert.dismiss()#关闭




