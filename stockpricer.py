import pandas as pd
import numpy as np
import requests
import math
import xlsxwriter
import os
import datetime 


adjusted_close = 0
volume = 0

def get_data(symbol):
    global adjusted_close
    global volume
    function = "TIME_SERIES_DAILY_ADJUSTED"
    outputsize = "compact"
    datatype = "json"
    base_url = 'https://www.alphavantage.co/query'
    api_key = os.getenv('API')
    api_url = f"{base_url}?function={function}&symbol={symbol}&outputsize={outputsize}&datatype={datatype}&apikey={api_key}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()

        data = response.json()
        time_series = data['Time Series (Daily)']

        stockdata = ""
        for date, values in time_series.items():
            stockdata += f"Date: {date}\n"
            formatted_date = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%B %d, %Y")
            stockdata += f"Formatted Date: {formatted_date}\n"
            stockdata += f"Open: {values['1. open']}\n"
            stockdata += f"High: {values['2. high']}\n"
            stockdata += f"Low: {values['3. low']}\n"
            stockdata += f"Close: {values['4. close']}\n"
            adjusted_close = values['5. adjusted close']
            stockdata += f"Adjusted Close: {adjusted_close}\n"
            volume = values['6. volume']
            stockdata += f"Volume: {volume}\n"
            stockdata += f"Dividend Amount: {values['7. dividend amount']}\n"
            stockdata += f"Split Coefficient: {values['8. split coefficient']}\n\n"
            break
        return stockdata
    
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except KeyError:
        print("Error: Failed to retrieve data from the API.")

def get_adjusted_close(symbol):
    get_data(symbol)
    return adjusted_close

def get_volume(symbol):
    get_data(symbol)
    return volume

