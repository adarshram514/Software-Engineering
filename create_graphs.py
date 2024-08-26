from grab_data_from_api import APIREQUESTS
import requests
from dotenv import load_dotenv
import os
import finnhub
from icecream import ic
import json
import matplotlib.pyplot as plt

class graph_creator():
    def __init__(self) -> None:
        self.grab_data = APIREQUESTS()
        pass

    def create_line_graph_us_spending(self,stock_name,start_time,end_time):
        #call the class inside of the us spending class
        us_spending_response = self.grab_data.get_us_spendnig(stock_name,start_time,end_time)
        
        
        x_axis = []
        y_axis = []
        
        #this will grab only the total value and actionDate and append it to the y-axis list to track amount given.
        for object in us_spending_response['data']:
            y_axis.append(object["totalValue"])
            x_axis.append(object["actionDate"])

        plt.plot(x_axis,y_axis)
        plt.xlabel("Dates Awareded")
        plt.ylabel("USD")
        plt.title(f"US spending for {stock_name}")

        x_ticks_to_show = [x_axis[0],x_axis[-1]]
        plt.xticks(x_ticks_to_show)
        plt.show()
