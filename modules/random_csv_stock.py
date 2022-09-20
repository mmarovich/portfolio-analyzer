import csv
import random


# function to return five random ticker symbols from a list of 30 non-MAANG ticker symbols
def stock_tickers_random():
    with open("data/stock_tickers_30.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        random_stock_list_30 = []
        for each_symbol in csv_reader:
            random_stock_list_30.append(each_symbol[0])
    random_stock_list_30
    random_stock_list_5 = random.sample(random_stock_list_30, k = 5)
    return random_stock_list_5