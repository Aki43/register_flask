import requests

seks = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open('dataset_3378_3.txt') as inf:
    t = inf.readline().strip()
t = requests.get(t).text
# print(t)
while 'we' not in t:
    t = requests.get(seks + t).text
    print(t)
