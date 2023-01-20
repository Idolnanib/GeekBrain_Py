import requests

responce = requests.get('https://gb.ru/education')

print(responce.text)