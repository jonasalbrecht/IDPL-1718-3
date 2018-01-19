from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def numberofsites(ps):
    searchsitescons = ps.findAll('a', {'title': lambda l: l and l.startswith('go to page ')})
    lastsite = 0
    numbers = []
    for x in searchsitescons:
        numbers.append(int(x['title'].replace('go to page ', '')))

    for num in numbers:
        if lastsite < num:
            lastsite = num
    return(lastsite)

def createurls(maxsite):
    myurls = []
    for i in range(1, maxsite):
        myurls.append('https://stackoverflow.com/questions/tagged/numpy?page={0}&sort=newest&pagesize=50'.format(i))

    return myurls

def createsoups(urls):
    mysoups = []
    for url in urls:
        print(url)
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        mysoups.append(soup(page_html, "html.parser"))
    return mysoups

def getquestionids(soups):
    containers = []
    for asoup in soups:
        containers.extend(
            asoup.findAll('a', {'class': 'question-hyperlink', 'href': lambda l: l and l.startswith('/questions/')}))
    questionids = []
    for f in containers:
        questionids.append(str(f['href']).split('/')[2])
    return questionids

myurl = 'https://stackoverflow.com/questions/tagged/numpy?page=1&sort=newest&pagesize=50'


uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")



maxint = numberofsites(page_soup)
myurls = createurls(maxint)
mysoups = createsoups(myurls)
myqids = getquestionids(mysoups)

qidtxt = open('qids.txt', 'w')
for qid in myqids:
    print(qid)
    qidtxt.write(qid + '\n')
qidtxt.close()



# f = open('StackOverFlowSearch.html', 'w')
# f.write(str(page_html))
# f.close()
    
# for x in containers:
#    l = x.findNext("meta", {"itemprop": lambda L: L and L.startswith("description")})
#    if (l["content"].startswith('Fu')):
#        fcontainers.append(x)

# f = open('htmldata.html', 'w')
# f.write(str(fcontainers[0]))
# f.close()

# for x in fcontainers:
#    print(x.meta["content"])
# name = containers[0].meta["content"]
# print(name)
