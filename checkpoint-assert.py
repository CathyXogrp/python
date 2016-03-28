from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from datetime import datetime
import time

LocalProfile = "C:\Users\csun\AppData\Roaming\Mozilla\Firefox\Profiles\zgn6rip8.default"
profile = FirefoxProfile(LocalProfile)
driver = webdriver.Firefox(profile)
driver.get("https://www.google.com.hk/")
#file_name = datetime.now().strftime("%Y_%m_%d_%H%M_Snapshot.PNG")
assert driver.title == "Google" 
#driver.save_screenshot(file_name)
driver.find_element_by_id("lst-ib").send_keys("theKnot")
driver.find_element_by_id("lst-ib").send_keys(Keys.ENTER)
time.sleep(10)
driver.find_element_by_css_selector("html body#gsr.vasq.srp div#viewport.ctr-p div#main.content div#cnt div.mw div#rcnt div.col div#center_col div#res.med div#search div div#ires div#rso div.g div div.rc h3.r a").click()
time.sleep(10)
assert driver.title in "The Knot"
