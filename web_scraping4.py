from bs4 import BeautifulSoup
import requests
import re

gpu = input("What product do you want to search for? ")

url = f"https://www.newegg.ca/p/pl?d={gpu}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text")
print(page_text)