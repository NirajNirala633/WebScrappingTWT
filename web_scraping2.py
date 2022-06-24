from bs4 import BeautifulSoup
import requests
import re

with open("./2/index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# tag = doc.find("option")

# result = doc.find_all("option")

# tag['value'] = 'new value'
# tag['selected'] = 'false'
# tag["color"] = "blue"
# print(tag.attrs)

# tag = doc.find_all(["p", "div", "li"]) 
# tag = doc.find_all("option", text="Undergraduate", value="undergraduate")

# tag = doc.find_all(class_="btn-item")

# tag = doc.find_all(text=re.compile("\$.*"))
# tag = doc.find_all(text=re.compile("\$.*"), limit=1)

# for ta in tag:
    # print(ta.strip())
 
# print(tag) 

tag = doc.find_all("input", type="text")
for ta in tag:
    ta["placeholder"] = "I changed you"

with open("./2/change.html", "w") as file:
    file.write(str(doc))