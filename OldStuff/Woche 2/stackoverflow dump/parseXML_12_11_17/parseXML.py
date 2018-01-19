from xml.dom import minidom
import re
from bs4 import  BeautifulSoup
# https://docs.python.org/2/library/xml.dom.html

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

class SOQuestion:

    def __init__(self, body, title, id):
        self.body = body
        self.title = title
        self.id = id
        self.answers = []  # SOAnswer[]
        self.bestAnswer = None  # SOAnswer
        #hasAnswers bool to do for some reasons (needs to be checked(best answer without answers))

    def printAnswers(self):
        for a in self.answers:
            print(a.body)

    def getID(self):
        return self.id

    def getBestAnswer(self):
        if len(self.answers) > 0:
            ba = self.answers[0]
            for a in self.answers:
                if a.score > ba.score:
                    ba = a
            return ba

    def filterHTMLtags(self):
        self.body = cleanhtml(self.body)
        for a in self.answers:
            a.body = cleanhtml(a.body)

    def filterHTMLtagsSoup(self):
        soup = BeautifulSoup(self.body, 'html.parser')
        self.body = soup.get_text()

class SOAnswer:

    def __init__(self, body, parentid, score):
        self.body = body
        self.parentid = parentid
        self.score = score

    def getParentID(self):
        return self.parentid


# parse xml
xmldoc = minidom.parse('Posts.xml')
# extract rows (posts)
rows = xmldoc.getElementsByTagName('row')

# initalize lists for questions and answers
SOQuestionList = []
SOAnswerList = []

# add questions to SOQuestionlist
# add answers to SOAnswerList
for row in rows:
     if row.hasAttribute('Title'):
         if 'numpy' in row.getAttribute('Body') or 'numpy' in row.getAttribute('Tags'):
            SOQuestionList.append(SOQuestion(row.getAttribute('Body'), row.getAttribute('Title'), int(row.getAttribute('Id'))))

     if row.hasAttribute('ParentId'):
         SOAnswerList.append(SOAnswer(row.getAttribute('Body'), int(row.getAttribute('ParentId')), int(row.getAttribute('Score'))))

# assign answers to questions
for q in SOQuestionList:
    for a in SOAnswerList:
        if q.getID() == a.getParentID():
            #print(str(q.id) + "?=" + str(a.parentid))
            q.answers.append(a)
            SOAnswerList.remove(a)

"""
# clean body (remove html tags)
for q in SOQuestionList:
    q.filterHTMLtags()
"""
# test clean with soup
SOQuestionList[1].filterHTMLtagsSoup()


print(SOQuestionList[1].body)
print(SOQuestionList[1].getBestAnswer().body)
