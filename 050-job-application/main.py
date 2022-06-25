from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "C:\Dev\chromedriver"
driver = webdriver.Chrome(executable_path = chrome_driver_path)

# Goto search results and sign-in
URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
driver.get(URL)
driver.maximize_window()

login_link = driver.find_element_by_link_text("Iniciar sesión")
login_link.click()
time.sleep(1)

username_input = driver.find_element(By.ID, "username")
username_input.send_keys("cdosorio@outlook.com")
pass_input = driver.find_element(By.ID, "password")
pass_input.send_keys("1234")
pass_input.send_keys(Keys.ENTER)
# login = driver.find_element_by_css_selector(".login__form_action_container button")
# login.send_keys(Keys.ENTER)
time.sleep(3)
 

# Scrolls down job list pane to load all listings and then returns to the top
job_list_scroll = driver.find_element_by_class_name("jobs-search__left-rail")
job_list_scroll.click()
html = driver.find_element_by_tag_name("html")
html.send_keys(Keys.END)
time.sleep(3)
html.send_keys(Keys.HOME)
 
 
# Gets all jobs on first page as clickable elements, clicks job, saves job, and repeats
job_list = driver.find_elements_by_css_selector(".job-card-container--clickable")
 
for job in job_list:
    job.click()
    time.sleep(1)
    save_button = driver.find_element_by_class_name("jobs-save-button")
    save_button.click()
    time.sleep(1)
 
driver.quit()
