from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.in/'

req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))