from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Dev\chromedriver"
driver = webdriver.Chrome(executable_path = chrome_driver_path)

driver.get("https://www.python.org/")

# search_bar = driver.find_element_by_name("q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")
# print(logo.size)

# about_link = driver.find_element_by_xpath('//*[@id="container"]/li[1]/a')
# print(about_link.text)


# Events dict
event_times = driver.find_elements_by_css_selector('.event-widget time') # by Class event-widget 
event_names = driver.find_elements_by_css_selector('.event-widget li a')
events = {}

# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text
#     }
events = { i: {'time': event_times[i].text, 'name': event_names[i].text} for i in range(0, len(event_names))}
print(events)

# with dict comprehension
# events = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul').text.splitlines()
# dictionary = { i: {'time': events[i], 'name': events[i+1]} for i in range(0, len(events), 2)}
# print(dictionary)

driver.quit()
