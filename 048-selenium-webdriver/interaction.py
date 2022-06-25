from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Dev\chromedriver"
driver = webdriver.Chrome(executable_path = chrome_driver_path)

#driver.get("https://en.wikipedia.org/wiki/Main_Page")

#article_count_link = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
#print(article_count_link.text)

# article_count = driver.find_element_by_css_selector("#articlecount a") #by ID articlecount
# print(article_count.text)


# ========= Click buttons ===========
# all_portals = driver.find_element(by=By.LINK_TEXT, value="Donate")
# all_portals.click()

# search_input = driver.find_element_by_name("search")
# search_input.send_keys("Python")
# search_input.send_keys(Keys.ENTER)


# ========= Fill form ===========
URL = "http://secure-retreat-92358.herokuapp.com/"
driver.get(URL)

forms = driver.find_element_by_name("fName")
forms.send_keys("Kino"+Keys.TAB+"Kowalski"+Keys.TAB+"jessi@wp.com"+Keys.TAB+Keys.ENTER)

#driver.quit()