import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get('http://quotes.toscrape.com/').text, 'lxml')
quotes = soup.find_all('span', {'class': 'text'})

print(len(quotes)) # 1번 print #
print(quotes[0].text) # 2번 print #
print(soup.find_all('div', {'class': 'quote'})[2].find('small').text) # 3번 print #