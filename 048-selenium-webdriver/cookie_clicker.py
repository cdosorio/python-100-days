from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
chrome_driver_path = "C:\Dev\chromedriver"
driver = webdriver.Chrome(executable_path = chrome_driver_path)
driver.get("https://eli-schwartz.github.io/cookieclicker/")

start = time.time()
time_limit = start + 20  # 60 * 5
 
def icon_click():
    """ Clicks on icon of last unlocked item """
    items = driver.find_elements(By.XPATH, '//*[@id="products"]/div')
    item_list = [i for i in items if i.get_attribute("class") == "product unlocked enabled"]
    item_list[-1].click()
 
 
def cookie_click():
    """ Starts 5 minute game timer and initiates cookie clicks, with icon clicks every 5 seconds.
     When complete, prints click speed """
    global time_limit
    while time.time() < time_limit:
        cookie = driver.find_element(By.ID, "bigCookie")
        now = time.time()
        future = now + 5
        while time.time() < future:
            cookie.click()
        icon_click()
        cookie_click()
    else:
        cookies = driver.find_element(By.ID, "cookies").text
        per_second = cookies.split(" ")[4]
        print(f"Cookies per second: {per_second}")
 
 
cookie_click()