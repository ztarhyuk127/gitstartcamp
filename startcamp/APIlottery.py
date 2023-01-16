import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1049'
data = requests.get(url).json()

for i in range(1,7):
    print(data.get(f"drwtNo{i}"))
print("보너스 번호 : ", data.get("bnusNo"))