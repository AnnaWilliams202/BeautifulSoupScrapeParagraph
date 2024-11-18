from bs4 import BeautifulSoup
import requests
from soupsieve import select

url = 'https://en.wikipedia.org/wiki/Mathematics'

result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')
#print(soup)

paragraphs = soup.select('p')
#print(paragraphs)

with open('paragraphs.txt', 'w') as file:
    for para in paragraphs[:7]:  # Only the first 7 paragraphs
        para_text = para.get_text()
        file.write(para_text + '\n')