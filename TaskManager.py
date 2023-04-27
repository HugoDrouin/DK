import datetime

from Scraper_b99 import Scraper_b99
import main  # to use "global variables"
from MyLogger import MyLogger

import urllib.request

import requests
import json

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
            #url = "https://bet99.com/en/sport-betting#/tree/all/0/674/0/0/odds/bytime"   javascript?
            #url = "https://betway.com/en/sports/sct/ufc---martial-arts/upcoming-fights" error 403
            #url = "https://www.sportsinteraction.com/mma-betting/" #error 403
            #url = "https://betway.com/api/Events/v2/GetEvents"
            #url = "https://www.888sport.com/ufc-mma/"  #must accept cookie, retourne code incompréhensible bytes? (cookie?)
            #url = "https://sports.bwin.com/en/sports/combat-sports-45" #retourne un cookie? bytes?
            #url = "https://stake.com/sports/mma/ufc" error 403
            #plusieurs plateformes demandent un login
            #headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            #                         '(KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            #           'Referer': 'http://www.google.com/',
            #           'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            #           'Accept-encoding': 'gzip, deflate, br',
            #           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,'
            #                     'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            #           }
            #response = requests.get(url, headers=headers)

            # BET99 - hidden API trouvé avec l'aide d'Insomnia :

            url = "https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEvents"
            querystring = {"timezoneOffset": "240", "langId": "8", "skinName": "bet99", "configId": "12",
                           "culture": "en-GB", "countryCode": "CA", "deviceType": "Mobile", "numformat": "en",
                           "integration": "bet99", "sportids": "0", "categoryids": "674", "champids": "0",
                           "group": "AllEvents", "period": "periodall", "withLive": "false", "outrightsDisplay": "none",
                           "marketTypeIds": "", "couponType": "0", "marketGroupId": "0"}
            payload = ""
            headers = {
                "authority": "sb2frontend-altenar2.biahosted.com",
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.9,fr;q=0.8",
                "origin": "https://bet99.com",
                "referer": "https://bet99.com/",
                "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A - Brand\";v=\"99\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
                              "(KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
            }
            response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

            if response.status_code != 200:
                print("Error fetching page")
                print(response.content)
                print(response.content.decode("UTF-16",errors="ignore"))
                exit()
            else:
                content = response.content
                print(content)
                with open('bet99_json.txt', 'w') as f:
                    f.write(response.text)
                    #f.write(str(content))
                    # print(content)
                #print(response.text)
                f.close()
        # Mode DEV - get content rom file
        else:
            # TODO : insert dans une BD test? Ou ne pas écrire du tout? ça dépend ce qu'on veut tester...
            local_file = "bet99_json.txt"
            #local_file = "MiseoJeu_zero_ev.txt"
            content = open(local_file, encoding="utf-8")
            logger.info(f'Ouverture du fichier local --{local_file}-- : réussie')

            #logger.info(content.read())

        # print html to file? for logging purposes?

        # Étape 3 parser le HTML pour générer une liste d'Event

        #scraper = Scraper_DK()
        #Scraper_DK.printMe("")
        scraper = Scraper_b99()
        #text = scraper.get_text(content) pas nécessaire avec hidden API
        #json = scraper.get_json(text) pas nécessaire avec hidden API. Nécessaire pour formattage?

        json_obj = scraper.get_json(content)  #attention json.load/loads
        offers_list = scraper.get_offers_list(json_obj)  # devrai ensuite ajouter les start dates avec 3 méthodes (complexe...)

        # TODO : ajouter startDate et startTime, puis intégrer dans le main branch

        # offers_list = []
        #offer_list returns ValueError if list is empty


        #offers_list = DataSeeker.getOffersFromHTML(content)
        #if len(offers_list) > 0:
        #    DBManager.insert_offers(offers_list)
        #else:
        #    msg = f'Aucune nouvelle offre disponible'
        #    logger.warning(msg)
