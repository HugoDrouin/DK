import logging

import bs4
import bs4 as bs
#import Event as Ev
from MyLogger import MyLogger

import urllib.request
logger = MyLogger(filename='myLog.log')

class Scraper_DK:

    #attributes
    url = ""
    json = ""
    offers_list = []

    # constructor
    def __init__(self):
        # initializing instance variable
        r = 6
        pass

    # Voir mon script Java et découper en plusieurs tâches (Chunks)
    # travailler avec json mal formé?
    #https: // stackoverflow.com / questions / 55553768 / parsing - out - specific - values -
    #from-json - object - in -beautifulsoup

    def getHTML(self,url):
        pass

    # Méthode spécifique à la structure du code html de DK
    def getJSON(self,html_content):
        logger.info("Exécution de getJSON(html_content)")
        soup = bs4.BeautifulSoup(html_content,'html.parser')
        script_elements = soup.find_all("script")

        # Trouver le text où les variables json sont écrites
        #f = open("out.txt", "w",encoding= "utf-8")
        #TODO catch exception si window. ... n'est pas trouvée
        for script in script_elements:
            if "window.__INITIAL_STATE__" in str(script):
                #f.write(str(script))
                script_str = str(script)
        #f.close()

        #subString = script_str.
        #String subString = scriptString.substring(scriptString.lastIndexOf("window.__INITIAL_STATE__"));

        index = script_str.rindex("window.__INITIAL_STATE__")
        subString = script_str[index:]

        #f = open("out2.txt", "w", encoding="utf-8")
        #f.write(subString)
        #f.close()

        # TODO : trimmer le début

        pass


   # wrapper les autres fonctions (privées) dans get_offers_list?
    def get_offers_list(json):
        pass

    @staticmethod
    def printMe(self):
        print("print me")

