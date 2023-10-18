from bs4 import BeautifulSoup

with open("website.html", encoding='utf8') as file:
    cotnents = file.read()

soup = BeautifulSoup(cotnents, "html.parser")
# print(soup.title.string)
##################################################################

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.getText())

##################################################################

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.get("href"))

##################################################################

# heading = soup.find(name="h1", id = "name")
# print(heading)

# section_heading = soup.find(name="h3",class_ = "heading")
# print(section_heading)

##################################################################

# #CSS Selectors
# company_url = soup.select_one(selector="p a")
# print(company_url)

# #CSS ID Selector
# name = soup.select_one(selector="#name")
# print(name)
 
# #CSS Class Selector
# headings = soup.select(".heading")
# print(headings)