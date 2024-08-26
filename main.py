from grab_data_from_api import APIREQUESTS
from icecream import ic
from create_graphs import graph_creator


grab_data = APIREQUESTS()

stock_name = 'AAPL'

##grab_data.get_stock_recommendation(stock_name)

start_date = "2023-01-01"
end_date = "2024-02-22"
j_object = grab_data.get_us_spendnig(stock_name,start_date,end_date)

#this can show all the possible keys inside the dictonaries
grab_data.get_all_headers_from_json_object(j_object)

header_set = {'actionDate', 'awardDescription'}

test = grab_data.parse_json_object(json_object=j_object,selected_headers=header_set)

graph_maker = graph_creator()
graph_maker.create_line_graph_us_spending(stock_name=stock_name,start_time=start_date,end_time=end_date)