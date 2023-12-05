import requests
from bs4 import BeautifulSoup

# URL of the Twitter feed
url = "https://twitter.com/your_twitter_feed"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the user names in the Twitter feed
user_names = soup.find_all("span", class_="username")

# Extract the text from the user names
user_names = [name.text for name in user_names]

# Print the user names
for name in user_names:
    print(name)
