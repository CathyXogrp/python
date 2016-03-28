# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.webdriver import FirefoxProfile
import unittest, time, re, random

class StoryWeddingEvent(unittest.TestCase):
    def setUp(self):
        LocalProfile ="C:\Users\csun\AppData\Roaming\Mozilla\Firefox\Profiles\zgn6rip8.default"
        profile = FirefoxProfile(LocalProfile)
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(30)
        self.base_url = "https://qa-beta.theknot.com/dashboard"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_story_wedding_event(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//ul[@id='mobile-nav']/div/div/li[8]/button").click()
        time.sleep(8)
        signup_frame = driver.find_element_by_css_selector("#modal > iframe")
        driver.switch_to_frame(signup_frame)
        driver.find_element_by_xpath("/html/body/div/div/main/div/section/div/form/p[2]/small/span[2]/a").click()
        time.sleep(2)
        driver.find_element_by_id("wizard_email").clear()
        driver.find_element_by_id("wizard_email").send_keys("kl@mailinator.com")
        driver.find_element_by_id("wizard_password").clear()
        driver.find_element_by_id("wizard_password").send_keys("aaaaaa")
        driver.find_element_by_name("button").click()
        driver.find_element_by_css_selector("li.nav-item.website > a").click()
        driver.find_element_by_xpath("//div[@id='right-blocks']/div/div/div[2]/div/p").click()
        driver.find_element_by_css_selector("div.gallery-add-title").click()
        e="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_id("story-title").clear()
        driver.find_element_by_id("story-title").send_keys(e)
        driver.find_element_by_css_selector("div.redactor-editor.redactor-placeholder").click()
        driver.find_element_by_id("save").click()
        driver.find_element_by_css_selector("ul.list-horizontal > li > a").click()
        #add wedding info
        driver.find_element_by_xpath("//div[@id='right-blocks']/div/div/div[2]/div[2]/p").click()
        driver.find_element_by_id("date-field").click()
        driver.find_element_by_xpath("//div[@id='recceremony']/div/div[2]/div/div/button").click()
        f="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_name("ceremony-venue-name").clear()
        driver.find_element_by_name("ceremony-venue-name").send_keys(f)
        g="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_name("reception-venue-name").clear()
        driver.find_element_by_name("reception-venue-name").send_keys(g)
        h="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_name("ceremony-full-address").clear()
        driver.find_element_by_name("ceremony-full-address").send_keys(h)
        i="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_name("reception-full-address").clear()
        driver.find_element_by_name("reception-full-address").send_keys(i)
        driver.find_element_by_css_selector("div.redactor-editor.redactor-placeholder > p").click()
        driver.find_element_by_id("save-wedding").click()
        driver.find_element_by_css_selector("ul.list-horizontal > li > a").click()
        #add event
        driver.find_element_by_xpath("//div[@id='right-blocks']/div/div/div[2]/div[3]/p").click()
        driver.find_element_by_css_selector("div.gallery-add-title").click()
        driver.find_element_by_id("date-input").click()
        driver.find_element_by_link_text("31").click()
        j="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_name("event-venue-name").clear()
        driver.find_element_by_name("event-venue-name").send_keys(j)
        driver.find_element_by_css_selector("div.redactor-editor.redactor-placeholder").click()
        driver.find_element_by_xpath("//div[@id='dialog-container']/div/div/div/div/div[3]/button").click()
        k="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_id("name-input").clear()
        driver.find_element_by_id("name-input").send_keys(k)
        driver.find_element_by_xpath("//div[@id='dialog-container']/div/div/div/div/div[3]/button").click()
        driver.find_element_by_css_selector("ul.list-horizontal > li > a").click()
        driver.find_element_by_xpath("//div[@id='right-blocks']/div/div[2]/div[2]/div[2]/p").click()
        driver.find_element_by_css_selector("div.gallery-add-title").click()
        l="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_id("item-name").clear()
        driver.find_element_by_id("item-name").send_keys(l)
        m="".join(random.sample("0236985741",10))
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys(m)
        driver.find_element_by_id("item-website").clear()
        driver.find_element_by_id("item-website").send_keys("www.baidu.com")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("fds@xogrp.com")
        driver.find_element_by_css_selector("p").click()
        driver.find_element_by_css_selector("div.button-container").click()
        driver.find_element_by_id("save-lc-item").click()
        driver.find_element_by_css_selector("ul.list-horizontal > li > a").click()
        time.sleep(30) 
        driver.find_element_by_xpath("//div[@id='right-blocks']/div/div[2]/div[2]/div[3]/p").click()
        driver.find_element_by_xpath("//div[@id='accommodations_list']/div/div[4]/div/div/div/div/div/div/div/img[2]").click()
        n="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_id("item-name").clear()
        driver.find_element_by_id("item-name").send_keys(n)
        o="".join(random.sample("85698746985",10))
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys(o)
        driver.find_element_by_xpath("//div[@id='add-lc-dialog']/div/div/div[2]/div[2]/div[2]").click()
        driver.find_element_by_id("item-website").clear()
        driver.find_element_by_id("item-website").send_keys("www.baidu.com")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("hgfd@xogrp.com")
        driver.find_element_by_css_selector("div.redactor-editor.redactor-placeholder").click()
        driver.find_element_by_id("save-lc-item").click()
        driver.find_element_by_css_selector("ul.list-horizontal > li > a").click()



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
