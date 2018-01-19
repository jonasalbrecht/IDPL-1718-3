import json
import unicodedata
from bs4 import BeautifulSoup
with open("arrays.ndarray.html") as doc:
    soup = BeautifulSoup(doc, "lxml")

rows = soup.find_all("tr")
list = []
for x in rows:

    c = unicodedata.normalize("NFKD", x.find('td').getText().replace("\u2019", ""))
    t = unicodedata.normalize("NFKC", x.find('td').find_next_sibling('td').getText().replace("\u2019", ""))
    list.append((c, t))

myjson = []

for x in list:
    if len(x[1]) > 0:
        myjson.append({'code': x[0], 'text': x[1]})

with open('data_arrays_ndarray.json', 'w+') as outfile:
    json.dump(myjson, outfile, indent=4)
