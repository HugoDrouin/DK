import json
#import Event as Ev
from MyLogger import MyLogger
import Offer

logger = MyLogger(filename='myLog.log')

class Scraper_b99:

    #attributes
    url = ""
    json = ""
    offers_list = []

    # constructor
    def __init__(self):
        # initializing instance variable
        r = 6
        pass

    @staticmethod
    def format_name(name):
        last_name = name[0:name.find(",")]
        first_name = name[name.find(",")+2:]
        return f'{first_name} {last_name}'
    @staticmethod
    def get_json(text):
        return json.load(text)

   # wrapper les autres fonctions (privées) dans get_offers_list?
    def get_offers_list(self, json_data):
        offers_dict = json_data['Result']['Items'][0]['Events']
        offers_list = []
        for offer in offers_dict:
            #event_name = offer['Name']  # à reformat
            startTime = offer['EventDate']
            # 2 types d'offres : Winner et Total (over/under)
            for item in offer['Items']:
                if (item['Name'] == 'Winner'):
                    #print(item)
                    outcome1 = item['Items'][0]['Name']
                    outcome1 = self.format_name(outcome1)
                    decimal_odds1 = item['Items'][0]['Price']

                    outcome2 = item['Items'][1]['Name']
                    outcome2 = self.format_name(outcome2)
                    decimal_odds2 = item['Items'][1]['Price']

                    #print(f'{outcome1} {decimal_odds1} {outcome2} {decimal_odds2}')
                    event_name = f'{outcome1} vs. {outcome2}'

                    #b99 ne semble pas distinguer le startTime et le StarDate
                    current_offer = Offer.Offer(startTime, startTime, event_name, outcome1,
                                                outcome2, decimal_odds1, decimal_odds2)
                    offers_list.append(current_offer)
        logger.info(f'{len(offers_list)} offres trouvées sur bet99/MMA/UFC')
        return offers_list


