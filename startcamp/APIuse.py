import requests #requests 모듈을 사용할게

url = 'https://api.agify.io?name=donghyuk&country_id=KR'

response = requests.get(url)
data = response.json() #딕셔너리!
print(data['age'], data['name']) #딕셔너리이므로 키를 통해 원하는 값만 출력 가능

# data = requests.get(url).json()

