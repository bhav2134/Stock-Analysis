import discord
import requests
import datetime

intents = discord.Intents.default()
intents.message_content = True 
client = discord.Client(intents=intents)
api_key = 'TOEIMD2DW5Z0USZG'
bot = 'MTExMTE4Mzg4MzkyNTQ2NzIyNg.GGEgsn.MUmE2pZfqJpTKCsnLAs9l0f8iU8BVKP_eQwiMc'


def get_data(symbol):
    function = "TIME_SERIES_DAILY_ADJUSTED"
    outputsize = "compact"
    datatype = "json"
    base_url = 'https://www.alphavantage.co/query'
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

      
@client.event
async def on_ready():
    print("Bot is ready {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content 

  if msg.startswith('$stock'):
    symbol = msg.split("$stock ", 1)[1]
    stockdatadc = get_data(symbol)
    await message.channel.send(stockdatadc)

client.run(bot)