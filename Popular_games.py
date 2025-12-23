from bs4 import BeautifulSoup

HTML_FILE = "Game_store_webpage.html"

with open(HTML_FILE, "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")
games=soup.ul.find_all("li")

for game in games:
    print (game.text)