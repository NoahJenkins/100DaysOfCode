from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/", )
# yc_webpage = response.text

# soup = BeautifulSoup(yc_webpage, "html.parser")
# # print(soup)
# article_tag = soup.find(name="span",class_="titleline")
# # print(article_tag)

# article_titles = []
# article_links = []
# for article_tag in soup.find_all(name="span", class_="titleline"):
#     article_titles.append(article_tag.getText())
#     article_links.append(article_tag.find("a")["href"])

# article_upvotes = []
# for article in soup.find_all(name="td", class_="subtext"):
#     if article.span.find(class_="score") is None:
#         article_upvotes.append(0)
#     else:
#         article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0]))

# max_points_index = article_upvotes.index(max(article_upvotes))
# print(
#     f"{article_titles[max_points_index]}, "
#     f"{article_upvotes[max_points_index]} points, "
#     f"available at: {article_links[max_points_index]}."
# )

h_news = response.text
soup = BeautifulSoup(h_news, "html.parser")
 
all_a_tags = soup.select(".titleline a")
 
href = []
titles = []
 
for tag in all_a_tags:
    if "http" in tag.get("href"):
        href.append(tag.get("href"))
        titles.append(tag.getText())

print(href, titles)