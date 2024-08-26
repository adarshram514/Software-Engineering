#Author: Sean Skaugen
#Organization: Cardassians
#Date: 2/20/24
#Conttact: 737-420-4619

import requests
from dotenv import load_dotenv
import os
import finnhub
from icecream import ic
import json

class APIREQUESTS():
    def __init__(self):
        """
        Initialize the APIRequests object.

        Args:None
        Description: creates a finnhub client object so it does not have to be instantiated at every method call.
        """
        self.finnhub_client = finnhub.Client(api_key=os.getenv("FIN_HUB_API_KEY"))
    
    """
    Get aggregate bars for a stock over a given date range in custom time window sizes.
    For example, if timespan = minute and multiplier = 5 then 5-minute bars will be returned.

    The start of the aggregate time window. Either a date with the format YYYY-MM-DD or a millisecond timestamp.
    sort = Sort the results by timestamp. asc will return results in ascending order (oldest at the top), desc will return results in descending order (newest at the top).
    """

    def get_stock(self,ticker,multiplier,timespan,start,end,sort):
        response = requests.get(f"https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?adjusted=true&sort=asc&limit=120&apiKey={self.api_key}")
        if response.status_code == 200:
            print("Got Data from server")
        else:
            print("sad")
    
    def get_stock_recommendation(self,stock_name):
        """
        Retrieves recommendation trends for a specific stock from the Finnhub API.

        This method queries the Finnhub API to fetch recommendation trends for the specified stock.

        Args:
            stock_name (str): The name or symbol of the stock for which recommendation trends are requested.

        Returns:
            dict: A list of dictionarys containing recommendation trends for the specified stock. 
                The dictionary typically includes the following keys:
                - 'buy': The number of analysts recommending to buy the stock.
                - 'hold': The number of analysts recommending to hold the stock.
                - 'sell': The number of analysts recommending to sell the stock.
                - 'strongBuy': The number of analysts recommending a strong buy.
                - 'strongSell': The number of analysts recommending a strong sell.
                - 'period': The time period covered by the recommendation trends.

            Example:
                {
                  'buy': 5,
                  'hold': 3,
                  'sell': 1,
                  'strongBuy': 2,
                  'strongSell': 0,
                  'period': '2024-02-22'
                }

        Raises:
        APIException: If there is an error while querying the Finnhub API.
        ValueError: If the provided stock_name is not a valid string or is empty.
        """
        json_response_object =self.finnhub_client.recommendation_trends(stock_name)

        ic(json_response_object)
    
    """
symbolREQUIRED
Symbol.

fromREQUIRED

From date YYYY-MM-DD. Filter for actionDate
toREQUIRED

To date YYYY-MM-DD. Filter for actionDate
    
    """
    def get_us_spendnig(self,stock_name,start_date,end_date):
        us_spending_response = self.finnhub_client.stock_usa_spending(stock_name,start_date,end_date)
        return us_spending_response
        ic(us_spending_response)

    def get_all_headers_from_json_object(self,json_object):
        """
        This will return a set with all possible headers that the user can select so they can fine tune searches.
        As the data that is returned by the json object may not be all useful.
        """
        all_keys_in_json_object = set()
        
        for key in json_object['data']:
            all_keys_in_json_object.update(key)
        
        return all_keys_in_json_object

    def parse_json_object(self,json_object,selected_headers):
        """
            This will return a list of dictonaries with only the seleted headers for the users.
        """
        parsed_data = []
        for object in json_object['data']:
            parsed_object = {}
            for header in selected_headers:
                if header in object:
                    parsed_object[header] = object[header]
            parsed_data.append(parsed_object)
        return parsed_data

            