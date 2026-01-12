import requests
from bs4 import BeautifulSoup

# news website
url = "https://www.lrt.lt/"

# request
response = requests.get(url)

# Parse
soup = BeautifulSoup(response.text, "html.parser")

#  Find headlines
headlines = soup.find_all(["h2", "h3"])

print("Top headlines from lrt.lt:\n")
for i, headline in enumerate(headlines, start=1):
    text = headline.get_text(strip=True)
    if text:
        print(f"{i}. {text}")
