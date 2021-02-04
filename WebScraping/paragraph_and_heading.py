from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.in/'

req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

print(soup.find_all('p'))

print(soup.find_all('h2'))