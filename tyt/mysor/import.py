import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/273.txt')
b = r.text.splitlines()
print(len(b))
