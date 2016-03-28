# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.webdriver import FirefoxProfile
import unittest, time, re, random

class Admin(unittest.TestCase):
    def setUp(self):
        LocalProfile ="C:\Users\csun\AppData\Roaming\Mozilla\Firefox\Profiles\zgn6rip8.default"
        profile = FirefoxProfile(LocalProfile)
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(30)
        self.base_url = "https://qa-beta.theknot.com/dashboard"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_admin(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//ul[@id='mobile-nav']/div/div/li[8]/button").click()
        time.sleep(8)#login
        signup_frame = driver.find_element_by_css_selector("#modal > iframe")
        driver.switch_to_frame(signup_frame)
        driver.find_element_by_xpath("/html/body/div/div/main/div/section/div/form/p[2]/small/span[2]/a").click()
        time.sleep(2)
        driver.find_element_by_id("wizard_email").clear()
        driver.find_element_by_id("wizard_email").send_keys("xc@mailinator.com")
        driver.find_element_by_id("wizard_password").clear()
        driver.find_element_by_id("wizard_password").send_keys("aaaaaa")
        driver.find_element_by_name("button").click()
        time.sleep(8)
        #go to WWS page
        driver.find_element_by_css_selector("li.nav-item.website > a").click()
        driver.find_element_by_css_selector("div.design-button-container > #preview").click()
        driver.find_element_by_xpath("//div[@id='preview-region']/div/div/div/div/div/div[2]/button").click()
        a="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_id("first-name").clear()
        driver.find_element_by_id("first-name").send_keys(a)
        b="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_id("last-name").clear()
        driver.find_element_by_id("last-name").send_keys(b)
        c="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_id("partner-first-name").clear()
        driver.find_element_by_id("partner-first-name").send_keys(c)
        d="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_id("partner-last-name").clear()
        driver.find_element_by_id("partner-last-name").send_keys(d)
        driver.find_element_by_id("wedding-location").clear()
        driver.find_element_by_id("wedding-location").send_keys("Sacramento, CA")
        time.sleep(5)
        driver.find_element_by_id("done").click()
        time.sleep(2)
        driver.find_element_by_id("done").click()
         
        
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
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
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
