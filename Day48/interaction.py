from selenium.common import exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#list of id using
#1. id = "saveMenu" -> menu
#2. cps -> return cookies/second
#3. store -> items like cursor, grandma



URL = "https://orteil.dashnet.org/experiments/cookie/"
driver = webdriver.Safari()
driver.get(URL)

# Find by CSS selector
items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_id = [item.get_attribute("id") for item in items]

current_time = time.time()
time_run = time.time() + 60 * 5

while True:
    cookie = driver.find_element(By.ID, value="cookie")
    cookie.click()

    if time.time() > current_time + 5:
        try:
            all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
            costs = []
            for price in all_prices:
                if price.text != "":
                    cost = int(price.text.split("-")[1].strip().replace(",", ""))
                    costs.append(cost)
        except exceptions.StaleElementReferenceException:
            continue  # Skip this iteration and retry

        store = {}
        for n in range(len(costs)):
            store[item_id[n]] = costs[n]

        cookie_count = driver.find_element(By.ID, value="money").text.replace(",", "")
        cookie_count_number = int(cookie_count)

        can_buy = {}
        for key, value in store.items():
            if value < cookie_count_number:
                can_buy[key] = value

        if can_buy:
            max_key = max(can_buy, key=can_buy.get)
            try:
                driver.find_element(By.ID, value=max_key).click()
            except exceptions.StaleElementReferenceException:
                continue  # Retry if element reference is stale

        current_time = time.time()

    if time.time() > time_run:
        try:
            click_count = driver.find_element(By.ID, value="cps").text
            print(click_count)
        except exceptions.StaleElementReferenceException:
            continue  # Retry if element reference is stale
        break

driver.quit()