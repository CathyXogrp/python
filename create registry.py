# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.webdriver import FirefoxProfile
import unittest, time, re, random

class Create(unittest.TestCase):
    def setUp(self):
        LocalProfile ="C:\Users\csun\AppData\Roaming\Mozilla\Firefox\Profiles\zgn6rip8.default"
        profile = FirefoxProfile(LocalProfile)
        self.driver = webdriver.Firefox(profile)
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qa-beta.theknot.com/dashboard"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_create(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//ul[@id='mobile-nav']/div/div/li[8]/button").click()
        time.sleep(8)
        signup_frame = driver.find_element_by_css_selector("#modal > iframe")
        driver.switch_to_frame(signup_frame)
        driver.find_element_by_xpath("/html/body/div/div/main/div/section/div/form/p[2]/small/span[2]/a").click()
        time.sleep(2)
        #driver.find_element_by_link_text("Log in").click()
        driver.find_element_by_id("wizard_email").clear()
        driver.find_element_by_id("wizard_email").send_keys("uuu@mailinator.com")
        driver.find_element_by_id("wizard_password").clear()
        driver.find_element_by_id("wizard_password").send_keys("aaaaaa")
        driver.find_element_by_name("button").click()
        time.sleep(8)   
        window_before = driver.window_handles[0]
        driver.find_element_by_xpath("(//a[contains(text(),'Registry')])[6]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'CREATE REGISTRY')])[5]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=wid1458530931462 | ]]
        window_after = driver.window_handles[1]
        driver.switch_to_window(window_after)
        driver.find_element_by_id("inspCreateReg").click()
        #step1
        driver.find_element_by_css_selector("html.js.flexbox.canvas.canvastext.webgl.no-touch.geolocation.postmessage.no-websqldatabase.indexeddb.hashchange.history.draganddrop.websockets.rgba.hsla.multiplebgs.backgroundsize.borderimage.borderradius.boxshadow.textshadow.opacity.cssanimations.csscolumns.cssgradients.no-cssreflections.csstransforms.csstransforms3d.csstransitions.fontface.generatedcontent.video.audio.localstorage.sessionstorage.webworkers.applicationcache.svg.inlinesvg.smil.svgclippaths body#home.grmBg.bootFix div.grmHeader.verticalNav div#viewport div#CreateRegistry.main-content.white div#tgt-CreateProcess.collegeRegistry.mainContainerMinHeight div.col-xs-8.column-left.tgt-left div#bb_mid_content.col-xs-8.col-xs-offset-2.tgt-createAccount.tgt-left.pL20 div.tgt-ButtonContainer.mTB40 a.tgtButton.btnPrimary.createprocessflow.col-xs-5.tgt-right.mR20").click()
        a="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys(a)
        b="".join(random.sample("qazwsxedcrfvtgb",3))
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys(b)
        c="".join(random.sample("qazwsxedcrfvtgb",3)) + '@.com'
        driver.find_element_by_id("CalogonId").clear()
        driver.find_element_by_id("CalogonId").send_keys(c)
        driver.find_element_by_id("CAlogonPassword").clear()
        driver.find_element_by_id("CAlogonPassword").send_keys("1q2w3e4r")
        driver.find_element_by_name("button").click()
        #step2
        time.sleep(5)
        driver.find_element_by_id("eventDate").send_keys("03/30/2016")
        driver.find_element_by_id("domesticRadioButton").click()
        driver.find_element_by_id("eventCity").send_keys("Sacramento")
        time.sleep(3)
        mySelect = Select(driver.find_element_by_id("eventState"))
        mySelect.select_by_visible_text("California")
        driver.find_element_by_css_selector("option[value=\"CA\"]").click()
        driver.find_element_by_id("numberOfGuests").clear()
        driver.find_element_by_id("numberOfGuests").send_keys("50")
        driver.find_element_by_name("button").click() 
        #step3
        time.sleep(3)
        d="".join(random.sample("qazwsxeikouhjmb",3))
        driver.find_element_by_id("coRegistrantFirstName").clear()
        driver.find_element_by_id("coRegistrantFirstName").send_keys(d)
        #driver.find_element_by_id("coRegistrantLastName").click()
        e="".join(random.sample("poiuytghjklmnbv",3))
        driver.find_element_by_id("coRegistrantLastName").clear()
        driver.find_element_by_id("coRegistrantLastName").send_keys(e)
        time.sleep(3)
        f="".join(random.sample("qazwsxeikouhjmb",3))
        driver.find_element_by_id("registrantFirstName").clear()
        driver.find_element_by_id("registrantFirstName").send_keys(f)
        #driver.find_element_by_id("coRegistrantLastName").click()
        g="".join(random.sample("poiuytghjklmnbv",3))
        driver.find_element_by_id("registrantLastName").clear()
        driver.find_element_by_id("registrantLastName").send_keys(g)
        time.sleep(3)
        mySelect = Select(driver.find_element_by_id("coRegistrantRole"))
        mySelect.select_by_visible_text("bride")
        time.sleep(3)
        mySelect = Select(driver.find_element_by_id("registrantRole"))
        mySelect.select_by_visible_text("groom")
        #Select(driver.find_element_by_id("coRegistrantRole")).select_by_visible_text("groom")
        driver.find_element_by_name("button").click()
        #step4
        driver.find_element_by_id("shippingAddressLine1").clear()
        driver.find_element_by_id("shippingAddressLine1").send_keys("13th ST")
        #driver.find_element_by_id("shippingCity").click()
        driver.find_element_by_id("shippingCity").clear()
        driver.find_element_by_id("shippingCity").send_keys("Sacramento")
        time.sleep(3)
        mySelect = Select(driver.find_element_by_id("shippingState"))
        mySelect.select_by_visible_text("California")
        driver.find_element_by_id("shippingZip").clear()
        driver.find_element_by_id("shippingZip").send_keys("94203")
        driver.find_element_by_id("registrantPhoneNumber").clear()
        driver.find_element_by_id("registrantPhoneNumber").send_keys("987-956-8596")
        driver.find_element_by_name("button").click()
        driver.find_element_by_id("useAsis_0").click()
        time.sleep(3)
    
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
