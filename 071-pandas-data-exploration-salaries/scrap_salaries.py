import requests
from bs4 import BeautifulSoup
import pandas as pd
 
records = []

endpoint = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
response = requests.get(endpoint)
soup = BeautifulSoup(response.text, "html.parser")
inner_btns = soup.find_all("div", {"class": "pagination__btn--inner"})
page_numbers = [inner_btn.getText() for inner_btn in inner_btns if inner_btn.getText().isnumeric()]
total_pages = int(max(page_numbers))

for current_page in range(total_pages):
    endpoint = f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{current_page + 1}"
    response = requests.get(endpoint)
    soup = BeautifulSoup(response.text, "html.parser")
 
    rows = soup.select("table.data-table tbody tr")
    for row in rows:
        cells = row.select("span.data-table__value")
        record = {
            "Undergraduate Major": cells[1].getText(),
            "Starting Median Salary": float(cells[3].getText().strip("$").replace(",", "")),
            "Mid-Career Median Salary": float(cells[4].getText().strip("$").replace(",", "")),
        }
        records.append(record)
 
pd.DataFrame(records).to_csv("salaries_by_college_major_updated.csv", index=False)