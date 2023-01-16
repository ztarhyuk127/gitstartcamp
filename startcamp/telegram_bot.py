import requests

token = "5874817630:AAFxRVJQ_wbi8JFBpAjJFDF5qaBQUOXQW0E"

url = f"https://api.telegram.org/bot{token}/getMe"

data = requests.get(url).json()
bot_id= data.get('result').get('id')
