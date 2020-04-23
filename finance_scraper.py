import requests 
from bs4 import BeautifulSoup 
import time
import pandas as pd



BASE_URL = "https://finance.yahoo.com/quote/{ticker}?p={ticker}"

def main():
    # Read list of tracked tickers 
    # TODO: replace with DB/settings file
    tickers = ["VOO","VFV.TO"]
    results = {}

    # For each ticker request and scrap web page
    for ticker in tickers:
      url = BASE_URL.format(ticker=ticker)
      soup = BeautifulSoup(requests.get(url).content, 'html.parser')

      field_price = soup.find('div', attrs={'id':'quote-header-info'}).find_all('span')[1].get_text()
      results[ticker] = float(field_price)

      # Wait a bit to avoid being banned
      time.sleep(2)


    for ticker in results:
      print("{ticker}: {price}".format(ticker=ticker, price=results[ticker]))


if __name__ == '__main__':
    main()