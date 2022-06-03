import requests
from bs4 import BeautifulSoup

def getRoomInfo(url):
    fields = getFields(url)
    sex = getSex(fields)
    languages = getLanguages(fields)

    return sex, languages

def getFields(url):
    page = requests.get(url)
    roomPage = BeautifulSoup(page.content, "html.parser")
    desiredTenantDiv = roomPage.find("div", class_="col s9")
    return desiredTenantDiv.find_all("tr")

def getSex(fields):
    return fields[1].find_next("td").find_next("td").text.strip()

def getLanguages(fields):
    result = []
    langs = fields[-1].find_next("td").find_next("td").find_all("div", class_="chip")

    for l in langs:
        result.append(l.text.strip())

    return result