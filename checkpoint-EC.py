from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import time

LocalProfile = "C:\Users\csun\AppData\Roaming\Mozilla\Firefox\Profiles\zgn6rip8.default"
profile = FirefoxProfile(LocalProfile)
driver = webdriver.Firefox(profile)
driver.get("https://qa-beta.theknot.com/dashboard")
file_name = datetime.now().strftime("%Y_%m_%d_%H%M_Snapshot.PNG")
try:
    WebDriverWait(driver, 10).until(EC.title_contains('The Knot'))
except TimeoutException:
    driver.save_screenshot(file_name)
    print 'check point fail 1'
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/header/nav/ul/div[1]/div/li[8]/button')))
except TimeoutException:
    driver.save_screenshot(file_name)
    print 'check point fail 2'
driver.find_element_by_xpath('/html/body/div[1]/div/header/nav/ul/div[1]/div/li[8]/button').click()
time.sleep(3)
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
time.sleep(8)
try:
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, '/html/body/div[1]/div/header/nav/ul/div[1]/div/li[8]/button')))
except TimeoutException:
    driver.save_screenshot(file_name)
    print 'check point fail 3'
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div[2]/section/div/div/div[1]/div[1]/div[2]/div/div/div/div[2]/ul/li[2]/a[1]')))
except TimeoutException:
    driver.save_screenshot(file_name)
    print 'check point fail 4'
try:
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div/main/div[2]/section/div/div/div[1]/div[1]/div[2]/div/div/div/div[2]/ul/li[3]/a')))
except TimeoutException:
    driver.save_screenshot(file_name)
    print 'check point fail 5'
try:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div[2]/section/div/div/div[1]/div[1]/div[2]/div/div/div/div[2]/ul/li[4]/a')))
except TimeoutException:
    driver.save_screenshot(file_name)
    print 'check point fail 6'
try:
    WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/section/div/div/div[1]/div[1]/div[2]/div/div/div/div[2]/ul/li[5]/a')))
except TimeoutException:
    driver.save_screenshot(file_name)
    print 'check point fail 7'
try:
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/div[1]/div/main/div[2]/section/div/div/div[1]/div[1]/div[2]/div/div/div/div[2]/ul/li[7]/a'),text_Budgeter))
except TimeoutException:
    driver.save_screenshot(file_name)
    print 'check point fail 8'
try:
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value((By.XPATH, '/html/body/div[1]/div/main/div[2]/section/div/div/div[1]/div[1]/div[2]/div/div/div/div[2]/ul/li[8]/a'),text_Inbox))
except TimeoutException:
    driver.save_screenshot(file_name)
    print 'check point fail 9'  
print 'pass'