import requests

token = "5874817630:AAFxRVJQ_wbi8JFBpAjJFDF5qaBQUOXQW0E"

url = f"https://api.telegram.org/bot{token}/getUpdates"

data = requests.get(url).json()

chat_id = data.get('result')[0].get('message').get('chat').get('id')

msg = '네.'

send_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"

requests.get((send_url))