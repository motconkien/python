from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_experimental_option("detach",True)

# driver = webdriver.Chrome(options=chrome_option)
# driver.get("https://wwww.amazon.com")

# driver.close()

driver = webdriver.Safari()
driver.get("https://www.amazon.com/nuphy-Portable-Mechanical-Compatible-Bluetooth/dp/B0CQRL2CDV/ref=sr_1_8?crid=AC9ROCYRUSU2&dib=eyJ2IjoiMSJ9.k7VYBM4zFjwhCn-yA8ZKSVEGUH7wYbVgTJqi7rJPSbUhZc5bFoDGguvyFasOYLFoo0TKgMCW6gYw22Bqb_4KSk5OdhuSA8YzUln3K71V4j7psvnCVzJOvyyCseP1lZzrHPijuaZrU2wmbN69Best4j0jnJyw9dKRIj2nMyXkXBIZc0nmlwwg27JUD3JFHqS4YkUSJU4T2To-dnr05MU-kRuo7G3VlkePqGMjHbYquEI.GQ9MwYrFk6EpvnvWaJb9_1ctBkXehuSML0d5tcD2sGM&dib_tag=se&keywords=keyboard+nuphy&qid=1721397255&sprefix=keyboard+nu%2Caps%2C300&sr=8-8")
price_dollar = driver.find_element(By.CLASS_NAME, value="a-offscreen")
print(price_dollar.text)



