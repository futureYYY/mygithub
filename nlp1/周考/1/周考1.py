import time

import requests
from bs4 import BeautifulSoup


myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

for i in range(1, 6):
    print(i)
    url = f"http://www.spiderbuf.cn/s04/?pageno={i}"
    print(url)
    html = requests.get(url, headers=myheaders).text
    print(html)

    with open(f'{i}.html', 'w', encoding='utf-8') as f:
        f.write(html)

    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('tr')

    with open(f'{i}.txt', 'w', encoding='utf-8') as f:
        for row in rows:
            columns = row.find_all('td')
            s = '|'.join(column.get_text() for column in columns)
            print(s)
            if s != '':
                f.write(s + '\n')



import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'http://www.spiderbuf.cn/s08/'

myheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

payload = {'level': '8'}
html = requests.post(url, headers=myheaders, data=payload).text

soup = BeautifulSoup(html, 'html.parser')
rows = soup.find_all('tr')


data = []
for row in rows:
    columns = row.find_all('td')
    row_data = [column.get_text() for column in columns]
    time.sleep(1)
    data.append(row_data)


df = pd.DataFrame(data)
# filename = 'data.csv'
df.to_csv('data.csv', index=False)
# print("Data has been successfully saved to", filename)

