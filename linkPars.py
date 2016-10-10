import requests
import re

URL = 'http://www.csd.tsu.ru/contacts'
f = requests.get(URL)
html = f.text
result2email = re.findall(r'(?:mailto:)(\w+@\w+(?:.\w+)+)', html)
print(result2email)



