from cgitb import strong
from unittest import result
from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080gaming-oc-10gd/p/N82E16814932459?Item=N82E16814932459&cm_sp=Homepage_dailydeals-_-P0_14-932-459-_-06232022&quicklink=true"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

# print(doc.prettify())

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong)
print(strong.string)
