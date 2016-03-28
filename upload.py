# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys#键盘
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException#处理元素异常，不是python的，是selenium的
from selenium.common.exceptions import NoAlertPresentException#处理弹框异常，不是python的，是selenium的
import unittest, time, re#re里的模块可以把屏幕里的内容进行分离
import os
class Upload(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qa-beta.theknot.com/dashboard"
        self.verificationErrors = []#建立列表 把错误保存到列表中
        self.accept_next_alert = True#处理弹窗
    
    def test_upload(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//ul[@id='mobile-nav']/div/div/li[8]/button").click()
        time.sleep(8)
        signup_frame = driver.find_element_by_css_selector("#modal > iframe")
        driver.switch_to_frame(signup_frame)
        driver.find_element_by_xpath("/html/body/div/div/main/div/section/div/form/p[2]/small/span[2]/a").click()
        time.sleep(2)
        driver.find_element_by_id("wizard_email").clear()
        driver.find_element_by_id("wizard_email").send_keys("zxc@mailinator.com")
        driver.find_element_by_id("wizard_password").clear()
        driver.find_element_by_id("wizard_password").send_keys("aaaaaa")
        driver.find_element_by_name("button").click()
        time.sleep(8)
        driver.find_element_by_css_selector("li.nav-item.website > a").click()
        driver.find_element_by_id("browse-designs").click()
        driver.find_element_by_css_selector("div.design-button-container > #preview").click()
        driver.find_element_by_xpath("//div[@id='preview-region']/div/div/div/div/div/div[2]/button").click()
        driver.find_element_by_id("upload-photo").click()
        driver.find_element_by_id("upload-button").click()
        driver.find_element_by_name("file").send_keys('D:\\test\upload_file.png')
        driver.find_element_by_id("fileupload").click()
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        driver.find_element_by_id("done").click()
        driver.find_element_by_id("first-name").click()
    
    def is_element_present(self, how, what):#判断页面元素是否找到
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):#处理弹窗
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):#获取弹窗的文本
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)#预期和实际做对比

if __name__ == "__main__":
    unittest.main()
