from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import datetime
 
chrome_driver_location = 'C:\Dev\chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_location)
 
endpoint = 'https://www.the-numbers.com/movie/budgets/all/'
 
# Get the last page number.
numbers = []
page_nos = []
current_page_no = 1
 
driver.get(f'{endpoint}{current_page_no}')
while True:
    try:
        page = driver.find_element_by_partial_link_text('»')
        page.click()
    except NoSuchElementException:
        page = driver.find_elements_by_class_name('pagination')
        for page_no in page:
            numbers = page_no.find_elements_by_tag_name('a')
        for number in numbers:
            page_nos.append(number.text)
        break
 
last_page = int(page_nos[-1][:5].replace(',', ''))
print(last_page, type(last_page))
 
 
movies = []
movie_info = []
movies_list = []
movies_in_current_page = []
rank = 1
 
# Get movie details as it is on the page.
while current_page_no < last_page + 1:
    driver.get(f'{endpoint}{current_page_no}')
    movies = driver.find_elements_by_tag_name('td')
 
    count = 0
    for info in movies:
        movie_info.append(info.text)
        count += 1
        if count == 6:
            record = {
                "Rank": movie_info[0],
                "Release_Date": movie_info[1],
                "Movie_Title": movie_info[2],
                "USD_Production_Budget": movie_info[3].strip(),
                "USD_Domestic_Gross": movie_info[4].strip(),
                "USD_Worldwide_Gross": movie_info[5].strip()
            }
 
            movies_in_current_page.append(record)
            movie_info.clear()
            count = 0
 
 
    # Change movie released date format and remove bad data like movies not yet released.
 
    for record in movies_in_current_page[:]:
        if record['Release_Date'] == 'Unknown':     
# Some movies have 'Unknown' in their release date column but year has been mentioned inside that movie page.
            # print(record)
            driver.find_element_by_link_text(record['Movie_Title']).click()
            year = driver.find_element_by_tag_name('h1')
            # print(year.text[-5:-1])
            try:
                record['Release_Date'] = datetime.datetime.strptime(year.text[-5:-1], '%Y').strftime("12/31/%Y")
            except ValueError:
                movies_in_current_page.remove(record)
            driver.back()
        else:
            try:
                record['Release_Date'] = datetime.datetime.strptime(record['Release_Date'], '%b %d, %Y').strftime(
                    "%m/%d/%Y")
            except ValueError:
                try:
                    record['Release_Date'] = datetime.datetime.strptime(record['Release_Date'], '%b, %Y').strftime(
                        "%m/01/%Y")
                except ValueError:
                    try:
                        record['Release_Date'] = datetime.datetime.strptime(record['Release_Date'], '%Y').strftime(
                            "12/31/%Y")
                    except ValueError:
                        movies_in_current_page.remove(record)
 
    # Update rank after bad data is removed.
    for record in movies_in_current_page:
        record['Rank'] = rank
        rank += 1
 
    movies_list.extend(movies_in_current_page)
    movies_in_current_page.clear()
    current_page_no += 100
 
# print(movies_list)
driver.quit()
 
# Create and save movie data to a .csv file.
pd.DataFrame(movies_list).to_csv("movies_2022.csv", index=False)