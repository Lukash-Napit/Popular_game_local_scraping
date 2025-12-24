from bs4 import BeautifulSoup

HTML_FILE = "Game_store_webpage.html"

with open(HTML_FILE, "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

cards = soup.find_all("div" , class_="card game")

for card  in cards:
    title = card.find("div",class_="title").text
    detail = card.find("div",class_="details").text
    print(title)
    print(f"{detail}\n")
