# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,random

class AccountSetting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qa-beta.theknot.com/dashboard"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_account_setting(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//ul[@id='mobile-nav']/div/div/li[8]/button").click()
        time.sleep(8)
        signup_frame = driver.find_element_by_css_selector("#modal > iframe")
        driver.switch_to_frame(signup_frame)
        driver.find_element_by_xpath("/html/body/div/div/main/div/section/div/form/p[2]/small/span[2]/a").click()
        time.sleep(2)
        driver.find_element_by_id("wizard_email").clear()
        driver.find_element_by_id("wizard_email").send_keys("zx@mailinator.com")
        driver.find_element_by_id("wizard_password").clear()
        driver.find_element_by_id("wizard_password").send_keys("aaaaaa")
        driver.find_element_by_name("button").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Account Settings')])[3]").click()
        a ="".join(random.sample("123456789",2))+"th,ST"
        driver.find_element_by_id("member_home_address_address_1").clear()
        driver.find_element_by_id("member_home_address_address_1").send_keys(a)
        b ="".join(random.sample("123456789",5))
        driver.find_element_by_id("member_home_address_zip").clear()
        driver.find_element_by_id("member_home_address_zip").send_keys(b)
        time.sleep(3)
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_css_selector("span[value=\"$5,001 - $10,000\"]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        driver.find_element_by_xpath("//div[@id='guest-dropdown']/ul/li[2]").click()
        time.sleep(3)
        driver.find_element_by_css_selector("html.js.flexbox.flexboxlegacy.canvas.canvastext.webgl.no-touch.geolocation.postmessage.no-websqldatabase.indexeddb.hashchange.history.draganddrop.websockets.rgba.hsla.multiplebgs.backgroundsize.borderimage.borderradius.boxshadow.textshadow.opacity.cssanimations.csscolumns.cssgradients.no-cssreflections.csstransforms.csstransforms3d.csstransitions.fontface.generatedcontent.video.audio.localstorage.sessionstorage.webworkers.applicationcache.svg.inlinesvg.smil.svgclippaths.breakpoint-desktop body.tk.logged-in div.wrapper div.main-content main section#account_settings_wrapper.container div#account_settings_page.container.col-md-9 div#account_settings_fields form#edit_member_personal_details.account_settings_form div#wedding_details.account-settings-group.desktop-display div.row.margin-bottom-22 div.col-md-6 div.account-settings-theme label.checkbox-label.checkbox-label-left label.fake-checkbox.icon.icon-checkbox").click()
        driver.find_element_by_css_selector("html.js.flexbox.flexboxlegacy.canvas.canvastext.webgl.no-touch.geolocation.postmessage.no-websqldatabase.indexeddb.hashchange.history.draganddrop.websockets.rgba.hsla.multiplebgs.backgroundsize.borderimage.borderradius.boxshadow.textshadow.opacity.cssanimations.csscolumns.cssgradients.no-cssreflections.csstransforms.csstransforms3d.csstransitions.fontface.generatedcontent.video.audio.localstorage.sessionstorage.webworkers.applicationcache.svg.inlinesvg.smil.svgclippaths.breakpoint-desktop body.tk.logged-in div.wrapper div.main-content main section#account_settings_wrapper.container div#account_settings_page.container.col-md-9 div#account_settings_fields form#edit_member_personal_details.account_settings_form div#wedding_details.account-settings-group.desktop-display div.margin-bottom-30 ul.color-selection.account-settings-colors li.color-swatch.red label.checkbox").click()
        driver.find_element_by_css_selector('html.js.flexbox.flexboxlegacy.canvas.canvastext.webgl.no-touch.geolocation.postmessage.no-websqldatabase.indexeddb.hashchange.history.draganddrop.websockets.rgba.hsla.multiplebgs.backgroundsize.borderimage.borderradius.boxshadow.textshadow.opacity.cssanimations.csscolumns.cssgradients.no-cssreflections.csstransforms.csstransforms3d.csstransitions.fontface.generatedcontent.video.audio.localstorage.sessionstorage.webworkers.applicationcache.svg.inlinesvg.smil.svgclippaths.breakpoint-desktop body.tk.logged-in div.wrapper div.main-content main section#account_settings_wrapper.container div#account_settings_page.container.col-md-9 div#account_settings_fields form#edit_member_personal_details.account_settings_form div.account-ui-buttons.desktop-display div.inner input.btn.btn-primary').click()
        time.sleep(15)
    
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
