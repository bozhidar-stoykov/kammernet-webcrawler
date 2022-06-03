import requests
from bs4 import BeautifulSoup

def getRoomURLs(url, filters):
    rooms = []
    mainPageResponse = requests.get(url)

    soupMP = BeautifulSoup(mainPageResponse.content, "html.parser")
    nbrPages = getNumberOfPages(soupMP)

    for pg in range(1, nbrPages+1):
        mainPage = routeToPage(url, pg)

        pageId = "search-results-page-" + str(pg)
        roomsPage = mainPage.find(id=pageId)
        rooms = rooms + getRooms(roomsPage)

    return extractURLfromRooms(rooms, filters)


def getNumberOfPages(soupMP):
    pagination = soupMP.find("ul", class_="pagination")
    if pagination == None:
        return 1
    else:
        pages = pagination.find_all("li")
        return (len(pages) - 1)


def routeToPage(url, pageNumber):
    if pageNumber == 1:
        url = url
    else:
        url = url + "?pageno=" + str(pageNumber)

    mainPageResponse = requests.get(url)
    mainPageHtml = BeautifulSoup(mainPageResponse.content, "html.parser")
    return mainPageHtml


def getRooms(roomsPage):
    return roomsPage.find_all(
        "div", class_="rowSearchResultRoom col s12 m6 l4"
    )


def extractURLfromRooms(rooms, filters):
    urls = []
    for r in rooms: 
        if matchFilters(r, filters):
            roomUrl = r.find("a", class_="tile-title truncate")
            urls.append(roomUrl["href"])

    return urls

def matchFilters(room, filters):
    maxPrice, minSize, inclGWE = filters
    price, textGWE, surface = getDetails(room)
    if price <= maxPrice and surface >= minSize:
        if inclGWE:
            if len(textGWE) > 1:
                return True
        else:
            return True

    return False


def getDetails(room):
    priceText = room.find("div", class_="tile-rent").text.strip()
    price = int(priceText.split(",")[0][2:])
    textGWE = priceText[8:]
    surface = int(room.find("div", class_="tile-surface").text.strip()[:-3])

    return price, textGWE, surface
    