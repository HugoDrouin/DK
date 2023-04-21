import bs4
import json
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

    def get_html(self,url):
        pass

    # input should be text correctly formatted in json
    # output : json object
    def get_json(self, text):
        logger.info("Exécution de get_json(text)")
        try:
            json_obj = json.loads(text)
        except:
            logger.error("Error converting text to json")
            return {}
        return json_obj


    # Méthode spécifique à la structure du code html de DK
    def get_text(self,html_content):
        logger.info("Exécution de get_text(html_content)")
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

        index = script_str.index("window.__INITIAL_STATE__")
        substring = script_str[index:]

        # trimmer le début
        index = substring.index("\"offers\":{")
        substring = "{" + substring[index:]

        # Trimmer la fin
        index = substring.index("}}},\"settings\"")
        substring = substring[:index+3]
        substring = substring + "}"

        #f = open("out2.txt", "w", encoding="utf-8")
        #f.write(substring)
        #f.close()

        return substring

   # wrapper les autres fonctions (privées) dans get_offers_list?
    def get_offers_list(self, DK_json):
        offers_dict = DK_json['offers']['9034']
        # Dans mon fichier test, il ya un seul event, eventID = 9034
        # for loop rudimentaire, pourrait être remplacé par une fonction récursive ou générique

        #Dk a des variables maisons : providerOfferID, offerID, etc. Je ne les banque pas pour l'insant
        for offer in offers_dict:
            #outcome1
            label1 = offers_dict[offer]['outcomes'][0]['label']
            oddsDecimal1 = offers_dict[offer]['outcomes'][0]['oddsDecimal']
            #outcome2
            label2 = offers_dict[offer]['outcomes'][1]['label']
            oddsDecimal2 = offers_dict[offer]['outcomes'][1]['oddsDecimal']

            event_name = f'{label1} vs {label2}'
            print(f'{event_name} {oddsDecimal1} {oddsDecimal2}')

        pass


