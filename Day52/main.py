from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time 
import os


similar_acc = "meolamdep_"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Safari()
        self.URL_Insta = "https://www.instagram.com/accounts/login/"
        self.gmail = "yannhuyenn@gmail.com"
        self.password = "1362081997"
    
    def login(self):
        self.driver.get(self.URL_Insta)
        try:
            email_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            print("Email input found")
            email_input.send_keys(self.gmail)
            
            pass_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            print("Password input found")
            pass_input.send_keys(self.password)
            
            pass_input.send_keys(Keys.ENTER)
            time.sleep(10)

            noti_prompt = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
            if noti_prompt:
                noti_prompt.click()

        except NoSuchElementException as e:
            print(f"Element not found: {e}")
       

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{similar_acc}/followers/")
        time.sleep(5)

        follower_path ="/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
        try:
            follower = WebDriverWait(self.driver,20).until(
                EC.presence_of_element_located((By.XPATH, follower_path))
            )
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"Other error: {e}")

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[1].scrollHeight", follower)
            time.sleep(2)

    def follow(self):
        try:
            dialog_container = WebDriverWait(self.driver,20).until(
                EC.presence_of_element_located((By.XPATH,"/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div"))
            )
            time.sleep(2)
            dialog = dialog_container.find_element(By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
            follow_buttons = dialog.find_elements(By.TAG_NAME, value='button')
            for element in follow_buttons:
                try:
                    element.click()
                    time.sleep(1)
                except ElementClickInterceptedException:
                    cancel_button = self.driver.find_element(By.XPATH, value='//button[contains(text(), "Cancel")]')
                    cancel_button.click()
                    time.sleep(1)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
    
    def close(self):
        self.driver.quit()

bot = InstaFollower()
bot.login()
time.sleep(5)
bot.find_followers()
time.sleep(10)
bot.follow()
time.sleep(20)
bot.close()