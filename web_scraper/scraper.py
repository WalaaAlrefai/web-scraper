import requests
import json
from bs4 import BeautifulSoup

url='https://en.wikipedia.org/wiki/History_of_Mexico'
page=requests.get(url)
# print (page.content)

soup= BeautifulSoup(page.content, 'html.parser')
# print (soup)
citations=soup.find_all('a', string ='citation needed')
print (citations)

def get_citations_needed_count(citations):
    citation_count=[]
    for citation in citations :
       result = citation.find('span')
       citation_count.append(result)
    return len(citation_count)


def get_citations_needed_report(citations):
    citation_report=[]
    for citation in citations :
       result = citation.find_parents('p')[0].text
       citation_report.append(result)
    return '\n'.join(citation_report).strip()

cleand_citations = [get_citations_needed_report(citations) for citation in citations]
data= json.dumps(cleand_citations)
with open('result.json','w') as file:
    file.write(data)
    

print (get_citations_needed_count(citations))
print (get_citations_needed_report(citations))


