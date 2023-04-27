from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from app import create_app, db
from app.models import Crypto

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
parameters = {
  'start':'1',
  'limit':'20',
  'listing_status':'active',
  'sort': 'cmc_rank'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '15daef1e-3fcc-46e5-8dcb-694f950ab633',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  list_coins = []
  for coin in data['data']:
    new_coin = Crypto(id=coin['id'], name=coin['name'], symbol=coin['symbol'], slug=coin['slug'], is_active=coin['is_active'], first_historical_data=coin['first_historical_data'], last_historical_data=coin['last_historical_data'])
    list_coins.append(new_coin)

  app = create_app()
  with app.app_context():
    db.session.add_all(list_coins)
    db.session.commit()

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)