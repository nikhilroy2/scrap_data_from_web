import json
from bs4 import BeautifulSoup
from urllib.request import urlopen


result = []

url = f'https://bsahercules.com/wp-content/plugins/superstorefinder-wp/ssf-wp-xml.php?wpml_lang=&t=1662871448251'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
#print(soup)

name = soup.select('item location')
address = soup.select('item address')
telephone = soup.select('item telephone')
email = soup.select('item email')
productsServices = soup.select('item productsServices')
for a,b,c,d,e in zip(name, address, telephone, email, productsServices):
    result.append({
        "name": a.text.replace(u'\xa0', u' '),
        "address": b.text.replace(u'\xa0', u' '),
        "telephone": c.text.replace(u'\xa0', u' '),
        "email": d.text.replace(u'\xa0', u' '),
        "productsServices": e.text.replace(u'\xa0', u' ')
    })

file = open('result.json', 'w')
file.write(str(result))
file.close()