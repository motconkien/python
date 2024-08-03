from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import os


PROMISDE_DOWN = 150
PROMISDE_UP = 10
gmail = os.environ.get("gmail")
password = os.environ.get("password")

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Safari()
        self.up = ""
        self.down = ""
        self.URL_seepd = "https://www.speedtest.net"
        self.URL_twitter = "https://x.com/login"
        self.wait = WebDriverWait(self.driver,60)
    
    def get_internet_speed(self):
        self.driver.get(self.URL_seepd)

        try:
            go_btn_container = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "start-button"))
            )
            go_btn = go_btn_container.find_element(By.CSS_SELECTOR, 'a')
           
            print("Found the go button. Clicking...")
            print("Clicking the go button using JavaScript...")
            self.driver.execute_script("arguments[0].click();", go_btn)

            time.sleep(60)
            result_container = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "result-container-data"))
            )
            print("Found result container. Extracting data...")

            # Extract the up and down speed values
            up_result = result_container.find_element(By.XPATH, '//span[@class="result-data-large number result-data-value download-speed"]')
            self.up = up_result.text

            down_result = result_container.find_element(By.XPATH, '//span[@class="result-data-large number result-data-value upload-speed"]')
            self.down = down_result.text

        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except TimeoutException as e:
            print(f"Timeout occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        # finally:
        #     self.driver.quit()  

    def tweet_at_provider(self):
        self.driver.get(self.URL_twitter)
        time.sleep(20)
        try:
            username_field = self.driver.find_element(By.NAME, "text")
            username_field.send_keys(gmail)
            username_field.send_keys(Keys.RETURN)

            time.sleep(10)

            password_field = self.driver.find_element(By.NAME, "password")
            password_field.send_keys(password)
            password_field.send_keys(Keys.RETURN)

            time.sleep(5)

            #tweet
            try:
                tweet_container = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')

                message = ""
                if self.down < PROMISDE_DOWN or self.up < PROMISDE_UP:
                    message += f"Hey Provider, why my internet speed down {self.down} Mbps - speed up {self.up} Mbps while I paid for {PROMISDE_DOWN} and {PROMISDE_UP}" 
                else:
                    message += f"Internet speed is good enough to down and up"
                tweet_container.send_keys(message)
                post_button = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
                time.sleep(2)
                post_button.click()
            except NoSuchElementException as e:
                print("Element tweet not found")

        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        # finally:
        #     self.driver.quit()
    
    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    print(f"Download Speed: {bot.down} Mbps - Upload Speed: {bot.up} Mbps")
    time.sleep(10)
    bot.tweet_at_provider()
    bot.close()
