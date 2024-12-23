from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_job_posted_inlinkedin():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.linkedin.com/jobs/search/?keywords=developer")
    
    job_posted = driver.find_elements(By.CLASS_NAME, "job-card-container__metadata-item")
    for job in job_posted:
        print(job.text)
    driver.quit()