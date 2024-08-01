from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
import time
import os

URL = "https://tinder.com"
fb_email = os.environ.get("mail")
fb_pass = os.environ.get("pass")

# Log in:
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
  print("More options is not found")

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
else:
    fb_btn.click()
    print(fb_btn)
    print("Clicked fb_btn")

time.sleep(10)

#switch window
print(driver.window_handles)
base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
print(driver.title)

time.sleep(10)

try:
  content_container = driver.find_element(By.ID, "content")
except NoSuchElementException:
  print("Can not be found by ID")
else:
   login_form_containter = content_container.find_element(By.CLASS_NAME,"login_form_container")
   email = login_form_containter.find_element(By.NAME,"email")
   password = login_form_containter.find_element(By.NAME,"pass")
   login_btn = login_form_containter.find_element(By.ID,"loginbutton")
   print("Sending keys")
   email.send_keys(fb_email)
   password.send_keys(fb_pass)
   login_btn.click()
   print("Log in")



#switch back to window
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(10)

# hitlike
for i in range(10):
  try:
        print("Clicking the Like button...")
        heart_icon = driver.find_element(By.XPATH, value="//*[@id='t2067052097']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button")
        heart_icon.click()

    # For "It's a match" pop-up!
  except ElementClickInterceptedException:
      try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()
      except NoSuchElementException:
            close_tinder= driver.find_element(By.XPATH, value="//*[@id='t338671021']/div/div[2]/div[2]/button")
            close_tinder.click()

  except NoSuchElementException:
      try:
            heart_icon = driver.find_element(By.XPATH, value="//*[@id='t2067052097']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button")
            heart_icon.click()
      except ElementClickInterceptedException:
            not_interested_button = driver.find_element(By.XPATH, value="//*[@id='t338671021']/div/div/div[2]/button[2]/div[2]/div[2]/div")
            not_interested_button.click()
driver.quit()
