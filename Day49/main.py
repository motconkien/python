from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd

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

job_count_element = driver.find_element(By.CSS_SELECTOR, ".jobsearch-JobCountAndSortPane-jobCount span")
    
job_count_text = job_count_element.text
print("Job Count Text:", job_count_text)
    
job_count_numeric = ''.join(filter(str.isdigit, job_count_text))
print("Job Count Numeric:", job_count_numeric)

#fetch data
element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".job_seen_beacon"))
    )


time.sleep(10)


jobs_dict = {'Job title': [], 'Company':[], 'Tag':[]}

def extract_tags():
    job_element = driver.find_elements(By.CSS_SELECTOR, '.job_seen_beacon')  
    for job in job_element:
        title = job.find_element(By.CSS_SELECTOR, 'h2.jobTitle').text
        company = job.find_element(By.CSS_SELECTOR, '[data-testid="company-name"]').text
        tag_containers = job.find_elements(By.CSS_SELECTOR, '.jobsearch-JobCard-tagContainer')
        for container in tag_containers:
            tags = container.find_elements(By.CSS_SELECTOR, '.jobsearch-JobCard-tag')
            tag_list = [tag.text for tag in tags ]

    jobs_dict['Job title'].append(title)
    jobs_dict['Company'].append(company)
    jobs_dict['Tag'].append(",".join(tag_list))
    # print(f"Title: {title} - company: {company} - tag: {tag_list}")
    return jobs_dict

def close_popup():
    try:
        close_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="閉じる"]')
        close_button.click()
        print("Popup closed")
    except NoSuchElementException:
        print("No popup found")

def next_page_extract_data():
    while True:
        close_popup()
        
        data = extract_tags()

        try:
            page_container = driver.find_element(By.CSS_SELECTOR,'nav[aria-label="pagination"]')
        except NoSuchElementException:
            print("No more pages found")
            break

        try:
            next_button = page_container.find_element(By.CSS_SELECTOR, 'a[data-testid="pagination-page-next"]')
            next_button.click()
            time.sleep(5)
        except(NoSuchElementException,StaleElementReferenceException):
            print("No pages remain")
            break
    
    return data

data = next_page_extract_data()
df = pd.DataFrame(data)
file = df.to_csv("Day49/job.csv",index=False)