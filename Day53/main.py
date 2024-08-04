from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

zillow_url = "https://appbrewery.github.io/Zillow-Clone/"
#create soup
response = requests.get(zillow_url)
raw_data = response.content
soup = BeautifulSoup(raw_data,"html.parser")

#fetch link a
links_container = soup.find_all("a")
zillow_a_tags = [a["href"].strip() for a in links_container if a['href'].startswith('https://www.zillow.com/')]

#fetch price
price_container = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
price_list = [price.text.split("/")[0].split(" ")[0].rstrip("+") for price in price_container]

#fetch address
address_container = soup.find_all("address")
address_list = [address.text.strip().replace('\n', '').replace('\t', '') for address in address_container]
# print(address_list)

#using selenium to fill
driver = webdriver.Safari()
for n in range(len(zillow_a_tags)):
    form_url = "https://forms.gle/h7cqRtBMo29XXaMX8"
    driver.get(form_url)
    time.sleep(20)
    try:
        address = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        submit_btn = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    
    except Exception as e:
        print(f"Error: {e}")
    else:
        address.click()
        address.send_keys(address_list[n])

        time.sleep(2)
        price.click()
        price.send_keys(price_list[n])
        
        time.sleep(2)
        link.click()
        link.send_keys(zillow_a_tags[n])

        time.sleep(2)
        submit_btn.click()
    finally:
        driver.close()