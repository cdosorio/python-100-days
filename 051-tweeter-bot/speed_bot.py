import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

SPEED_TEST_URL = "https://www.speedtest.net/"

class SpeedTestBot:
  def __init__(self, driver_path):
    self.driver = webdriver.Chrome(executable_path = driver_path)

  def get_internet_speed(self):
    self.driver.get(SPEED_TEST_URL)
    self.driver.maximize_window()
    time.sleep(5)
    
    try:            
      start_btn = self.driver.find_element_by_class_name("start-text")
      start_btn.click()
    except NoSuchElementException:
      print("Couldn't click on the start button.\n" + NoSuchElementException)

    time.sleep(60)
    print("Searching test result..")

    #close dismiss
    # try:
    #   print(x)
    # except NoSuchElementException:
    #   pass

    self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
    self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)

    print(f"Down: {self.down} Mbps\nUp: {self.up} Mbps")
  