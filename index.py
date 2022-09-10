import urllib, json

sample = 'https://api.github.com/users/hadley/orgs'
url = 'https://www.herocycles.com/admin/public/api/stores?name=&email=&mobile=&city=&state=&limit=15&page=1.json'


response = urllib.urlopen(sample)

data = json.loads(response.read())

print(data)