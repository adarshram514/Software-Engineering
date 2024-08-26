import os
from dotenv import load_dotenv
import requests

class NEWS():
    def __init__(self) -> None:
        load_dotenv()
        self.api_key = os.getenv("NEWS_API_KEY")
        self.base_url = "https://newsdata.io/api/1/news?apikey="


    def get_news(self, wanted_news):
        '''This function will return the news from the API

        Args:
            wanted_news (str): The news that you want to get from the API
            API_KEY (str): The API key used to access the API
        
        Returns: Response from the API in JSON format

        Raises:

        '''

        #leave the s&q= after api.key to avoid errors
        url = f"{self.base_url}{self.api_key}&q={wanted_news}&country=us&image=1"

        payload = {}
        headers = {}

        try:
            response = requests.request("GET", url, headers=headers, data=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'An error occurred: {e}')

'''
Debugging code
get_news = NEWS()
news_json = get_news.get_news("CryptoCurrency")
print(news_json)
'''