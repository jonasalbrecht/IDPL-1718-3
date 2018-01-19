from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json

def createquestionurls(ids):
    questionurls = []
    for id in ids:
        questionurls.append("https://stackoverflow.com/questions/{0}".format(str(id)))
    return questionurls

def createjson(urls):
    jsonposts = []
    i = 0
    for url in urls:
        i += 1
        print("[" + str(i) + "|" + str(len(urls)) + "]")
        try:
            uClient = uReq(url)
            page_html = uClient.read()
            uClient.close()
        except:
            continue
        page_soup = soup(page_html, "html.parser")
        question = page_soup.find('div', {'class': 'question'})
        question = question.find('td', {'class': 'postcell'})

        answers = page_soup.findAll('td', {'class': 'answercell'})
        jsonpost = {'pID': 0,
                    'question': str(question),
                    'answers': [str(a) for a in answers]
                    }
        jsonposts.append(jsonpost)
    jsondataobj = {'data': jsonposts}

    with open('data.json', 'w+') as json_file:
        jsoned_data = json.dumps(jsondataobj, indent=True)
        json_file.write(jsoned_data)

idtxt = open('qids.txt', 'r')
lines = idtxt.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")

urls = createquestionurls(lines)

createjson(urls)



# questiontext = question.findAll('p')
# questiontext = [q.getText() for q in questiontext]

# questioncode = question.findAll('code')
# questioncode = [c.getText() for c in questioncode]

# jsonresult = {'qID': 0,
#                 'question':{
#                     'qtext': questiontext,
#                     'qcode': questioncode
#                 }
#               }
# jstring = json.dumps(jsonresult,sort_keys=True, indent=4, separators=(',', ': '))
# print(str(jstring))

# answers = page_soup.findAll('div', {'class': 'answer'})
# print(answers)

# print("len answers:" + str(len(answers)))
# with open('data.json', 'w') as f:
#     json.dump(jstring, f)