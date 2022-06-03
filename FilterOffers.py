def filterOffers(sex, langs, url, sexF):
    if sex == sexF or sex == "Niet belangrijk":
        lang = getLanguage(langs)
        if lang == "English" or lang == "Not significant":
            printOffer(sex, lang, url)

def getLanguage(langs):
    if "Engels" in langs:
        return "English"
    elif len(langs) == 0:
        return "Not significant"
    else:
        return "Other"

def printOffer(sex, lang, url):
    print("\nLink: " + url)
    #print("Sex: " + sex)
    #print("Languages: " + lang)