from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

URL = "https://tinder.com"
fb_email = "thanhhuyenclinic@gmail.com"
fb_pass = "huyen@20897"

# com: 
#   Log in:
driver = webdriver.Safari()
driver.set_window_size(800,600)
driver.get(URL)

# Wait for the page to load
time.sleep(5)

driver.implicitly_wait(10)

accept_btn = driver.find_element(By.XPATH, "//div[contains(text(), 'I accept')]/ancestor::button")
if accept_btn:
    accept_btn.click()
    print("Clicked accept_btn")

login_btn = driver.find_element(By.XPATH, "//div[@class = 'Expand']//button[.//div[contains(text(),'Log in')]]")
if login_btn:
    login_btn.click()
    print("Clicked login_btn")

# Wait for login more
time.sleep(5)

more_btn = None
try:
  more_btn = driver.find_element(By.XPATH, "//div[@class = 'Mt(a)']//button[contains(text(),'More Options')]")
except NoSuchElementException:
  print("Mpre options is not found")

if more_btn:
    more_btn.click()
    print("Clicked more_btn")


# Wait for clicked more
time.sleep(5)

fb_btn = None
try:
  fb_btn = driver.find_element(By.XPATH, "//div[@class = 'Mt(a)']//button[@aria-label='Log in with Facebook']")
except NoSuchElementException:
  print("fb_btn is not found")

if fb_btn:
    fb_btn.click()
    print(fb_btn)
    print("Clicked fb_btn")


fbx_btn = None
try:
  fbx_btn = driver.find_element(By.XPATH, "//div[@class = 'Mt(a)']//button[@aria-label='Login with Facebook']")
except NoSuchElementException:
  print("fbx_btn is not found")

if fbx_btn:
    fbx_btn.click()
    print("Clicked fbx_btn")
time.sleep(10)
base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
print(driver.title) 

#switch window
print(driver.window_handles)
base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
print(driver.title)
time.sleep(10)
email = driver.find_element(By.XPATH,'//input[@id="email"]')
password = driver.find_element(By.XPATH,'//input[@id="pass"]')
btn_login = driver.find_element(By.XPATH,'//input[@name="login"]')
print("Sending keys")
email.send_keys(fb_email)
password.send_keys(fb_pass)
btn_login.click()
driver.switch_to.window(base_window)
