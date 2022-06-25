from bs4 import BeautifulSoup
#import lxml

with open("website.html", encoding="utf-8") as file:
    content = file.read()
    #print(content)

soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.prettify())

all_anchor_tags = soup.find_all("a")
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

# Find by ID
# heading = soup.find(name="h1", id="name")
# print(heading)

# # Find by class
# h3_heading = soup.find(name="h3", class_="heading")
# print(h3_heading.getText())

# # using CSS selectors
# company_url = soup.select_one(selector="p a")
# print(company_url)

# name =  soup.select_one("#name") # by id
# print(name)

# headings = soup.select(".heading") # all, by class
# print(headings)

# Get value of attribute
# form_input = soup.find("input")
# max_length = form_input.get("maxlength")






