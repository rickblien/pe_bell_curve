import requests

class income_statement:

    def __init__(self, symbol):
        self.Base_URL = 'https://www.macrotrends.net/stocks/charts/'
        self.symbol = symbol

    def get_eps(self):
        url = f"{self.BASE_URL}/{self.symbol}/{self.symbol}/eps-earnings-per-share-diluted"
        r = requests.get(url)

        return r.json()

# class balance_sheet:


# class cash_flow_statement:
