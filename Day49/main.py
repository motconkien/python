from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

URL = "https://jp.indeed.com/?r=us"
driver = webdriver.Safari()
driver.get(URL)


search = driver.find_element(By.XPATH,'//*[@id="text-input-what"]')
search.send_keys("data analyst")
search.send_keys(Keys.ENTER)


wait = WebDriverWait(driver, 10)
element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".jobsearch-JobCountAndSortPane-jobCount"))
    )

# Find the element that contains the value "200"
job_count_element = driver.find_element(By.CSS_SELECTOR, ".jobsearch-JobCountAndSortPane-jobCount span")
    
# Extract and print the text value
job_count_text = job_count_element.text
print("Job Count Text:", job_count_text)
    
# Extract only the numeric part if necessary
job_count_numeric = ''.join(filter(str.isdigit, job_count_text))
print("Job Count Numeric:", job_count_numeric)

#fetch data
element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#mosaic-provider-jobcards > ul"))
    )
job_elements = driver.find_elements(By.CSS_SELECTOR, '#mosaic-provider-jobcards > ul li')  # Adjust CSS selector as needed
# for job in job_elements:
#     title = job.find_element(By.CSS_SELECTOR, 'h2.jobTitle').text
#     company = job.find_element(By.CSS_SELECTOR, '.companyName').text
#     print(f"Title: {title}, Company: {company}")
time.sleep(10)
job_element = driver.find_elements(By.CSS_SELECTOR, '.job_seen_beacon')  # Adjust CSS selector as needed
for job in job_element:
    title = job.find_element(By.CSS_SELECTOR, 'h2.jobTitle').text
    company = job.find_element(By.CSS_SELECTOR, '[data-testid="company-name"]').text

    # company = job.find_element(By.CSS_SELECTOR, '.company-name').text
    print(f"Title: {title} - company: {company}")
    
