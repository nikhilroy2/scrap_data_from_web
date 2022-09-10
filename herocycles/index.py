import requests
from bs4 import BeautifulSoup

result = []
for i in range (1,5):
    page = requests.get(f'https://www.herocycles.com/admin/public/api/stores?name=&email=&mobile=&city=&state=&limit=15&page={i}')
    soup = BeautifulSoup(page.content, 'html.parser')    
    for r in soup.find_all():
        result.append(r)
print(result)


# import requests
# from bs4 import BeautifulSoup as bs
# page = 1
# titles = []
# for i in range(1,5):
#       url = f"https://www.bookdepository.com/bestsellers?page={page}"
#       response = requests.get(url)
#       html = response.content
#       soup = bs4(html, "lxml")
#       for h3 in soup.find_all("h3", class_="title"):
#             titles.append(h3.get_text(strip=True))
#       page = page + 1

# print(titles)