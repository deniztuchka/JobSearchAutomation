from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

driver = webdriver.Chrome()

username = "your_email"
password = "your_password"

def login_to_linkedin():
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)
    
    email_field = driver.find_element_by_id("username")
    email_field.send_keys(username)
    
    password_field = driver.find_element_by_id("password")
    password_field.send_keys(password)
    
    password_field.send_keys(Keys.RETURN)
    time.sleep(2)

def search_jobs(keyword, location):
    driver.get("https://www.linkedin.com/jobs/")
    time.sleep(2)
    
    search_field = driver.find_element_by_css_selector('input.jobs-search-box__text-input')
    search_field.send_keys(keyword)
    
    location_field = driver.find_element_by_css_selector('input.jobs-search-box__text-input--location')
    location_field.clear()
    location_field.send_keys(location)
    location_field.send_keys(Keys.RETURN)
    
    time.sleep(3)
    
def extract_job_info():
    jobs = driver.find_elements_by_class_name('result-card')
    job_list = []
    
    for job in jobs:
        title = job.find_element_by_class_name('job-result-card__title').text
        company = job.find_element_by_class_name('result-card__subtitle').text
        link = job.find_element_by_class_name('result-card__full-card-link').get_attribute('href')
        
        job_list.append([title, company, link])
    
    return job_list

def save_to_csv(job_list):
    with open("job_listings.csv", mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company", "Link"])
        writer.writerows(job_list)

if __name__ == "__main__":
    login_to_linkedin()
    search_jobs("Python Developer", "Remote")
    job_data = extract_job_info()
    save_to_csv(job_data)
    driver.quit()
