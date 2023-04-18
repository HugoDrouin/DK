import datetime

from Scraper_DK import Scraper_DK
import main  # to use "global variables"
from MyLogger import MyLogger

import urllib.request

import requests

#import Event as Ev
#from DataSeeker import DataSeeker
#from DBManager import DBManager

logger = MyLogger(filename='myLog.log')


class TaskManager:

    @staticmethod
    def run():
        # Étape 2 - Get source HTML code

        # if mode = DEV, input html from a file
        # else if mode = PROD input HTML pour URL

        if main.global_mode == "PROD":
            logger.info(main.global_mode)
            # TODO : METTRE LES HEADERS AILLEURS POUR AMÉLIORER LA LISIBILITÉ
            f = open("htmlResponse.txt", "w")
            url = "https://miseojeu.espacejeux.com/fr/offre-de-paris/combat/arts-martiaux-mixtes?idAct=45"
            headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                     '(KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                       'Referer': 'http://www.google.com/',
                       'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
                       'Accept-encoding': 'gzip, deflate, br',
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,'
                                 'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                       }
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                print("Error fetching page")
                print(response)
                exit()
            else:
                content = response.content
                f.write(str(content))
                # print(content)
                # print(response.text)
                f.close()
        # Mode DEV - get content rom file
        else:
            # TODO : insert dans une BD test? Ou ne pas écrire du tout? ça dépend ce qu'on veut tester...
            local_file = "DK_test_html.txt"
            #local_file = "MiseoJeu_zero_ev.txt"
            content = open(local_file, encoding="utf-8")
            logger.info(f'Ouverture du fichier local --{local_file}-- : réussie')

            #logger.info(content.read())

        # print html to file? for logging purposes?

        # Étape 3 parser le HTML pour générer une liste d'Event

        #scraper = Scraper_DK()
        Scraper_DK.printMe("")




        # offers_list = []
        #offer_list returns ValueError if list is empty


        #offers_list = DataSeeker.getOffersFromHTML(content)
        #if len(offers_list) > 0:
        #    DBManager.insert_offers(offers_list)
        #else:
        #    msg = f'Aucune nouvelle offre disponible'
        #    logger.warning(msg)
