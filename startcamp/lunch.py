import random

menu = ["치킨", "피자", "마라탕", "삼겹살"]

print(menu)
print(len(menu))
print(menu[0], menu[2])

pick = random.choice(menu)
print(pick)