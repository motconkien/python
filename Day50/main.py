from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

URL = "https://tinder.com"
fb_email = "thanhhuyenclinic@gmail.com"
fb_pass = "huyexxxx"
driver = webdriver.Safari()
driver.get(URL)

# Wait for the page to load
time.sleep(5)

wait = WebDriverWait(driver, 60)


def close_popup(): 
    try:
        accept_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'I accept')]/ancestor::button")))
        if accept_btn:
            accept_btn.click()
            print("Click accept btn")
    except NoSuchElementException:
        print("Not found")


try:
    close_popup()
    login_btn = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,"//div[@class = 'Expand Pos(r)']//button[.//div[contains(text(),'Log in')]]")
        )
    )

except NoSuchElementException:
    print("Not found")
else:
    if login_btn:
        login_btn.click()
        print("Click log in")

        try:
            fb_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//div[@class = 'Mt(a)']//button[.//div[contains(text(), 'Log in with Facebook')]]")))
            if fb_btn:
                fb_btn.click()
                print("found")
        except NoSuchElementException:
            print("Not found")
        else:
            time.sleep(10)
            base_window = driver.window_handles[0]
            fb_window = driver.window_handles[1]
            driver.switch_to.window(fb_window)
            print(driver.title)

            email = driver.find_element(By.XPATH, '//*[@id="email"]')
            password = driver.find_element(By.XPATH, '//*[@id="pass"]')
            # btn = driver.find_element(By.XPATH,'//*[@id="buttons"]')
            email.send_keys(fb_email)
            password.send_keys(fb_pass)
            password.send_keys(Keys.ENTER)
            # btn.click()

            driver.switch_to.window(base_window)
            print(driver.title)

            time.sleep(5)
            allow_location = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Allow' and @data-testid='allow']"))
            )
            allow_location.click()

            noti_btn = driver.find_element(By.XPATH,"//button[@aria-label='I'll miss out' and @data-testid='decline']")
            noti_btn.click()

            # for n in range(10):
            #     time.sleep(2)

            #     try:
            #         print("Called")
            #         like_btn = wait.until(
            #                         EC.element_to_be_clickable((
            #                             By.XPATH,'(//div[contains(@class, "Pos(a) B(0) Iso(i) W(100%) Start(0) End(0)")]/div/div/button)[4]')
            #                     )
            #                 )
            #         like_btn.click()
            #     except NoSuchElementException:
            #         print("not found")

