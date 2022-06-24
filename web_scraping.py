from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# tag = doc.title
# tag.string = "Hello!"
# print(tag)   
# print(tag.string)    

gat = doc.find("a")
gate = doc.find_all("a")

print(gate)
print(gat)


# print(doc.prettify())   