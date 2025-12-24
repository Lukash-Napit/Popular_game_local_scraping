from bs4 import BeautifulSoup

HTML_FILE = "Game_store_webpage.html"

with open(HTML_FILE, "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")
titles=soup.find_all("div" , class_="title")


for title in titles:
    print (title.text)
