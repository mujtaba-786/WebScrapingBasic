from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.in/'

req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

for img in soup.find_all('img'):
    print(img.get('src'))
