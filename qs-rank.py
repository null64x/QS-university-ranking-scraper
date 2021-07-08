import csv

import requests
from bs4 import BeautifulSoup
import io
import pandas as pd

url = 'https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/3740566.txt?1624879808?v=1625562924528'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 "
                         "Safari/537.36"}

file = open("qs-rank.txt", "w")

path = 'C:/Users/DELL/PycharmProjects/scrapeQS/qs-rank.txt'


def get_page(url):
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.json()
    except requests.ConnectionError as e:
        print(e)


def parser_page(json):
    if json:
        items = json.get('data')
        for i in range(len(items)):
            item = items[i]
            qsrank = {}
            if "=" in item['rank_display']:
                rk_str = str(item['rank_display']).split('=')[-1]
                qsrank['rank_display'] = rk_str
            else:
                qsrank['rank_display'] = item['rank_display']
            qsrank['logo'] = item['logo']
            qsrank['title'] = BeautifulSoup(item['title'], "html.parser").text
            qsrank['region'] = item['region']
            qsrank['score'] = item['score']



            yield qsrank


def main():
    json = get_page(url)
    results = parser_page(json)
    for result in results:
        with io.open(path, 'a', encoding="utf-8") as f:
            f.write(result['rank_display'] + ';' + 'www.https://www.topuniversities.com' + result['logo'] + ';' + result['title'] + ';' + result['region'] + ';' + result['score'] + '\n')
            f.close()
            print(result)


if __name__ == '__main__':
    print('Started parsing！')
    with io.open(path, 'a', encoding="utf-8") as f:
        f.write('Ranking' + ';' +'logo' + ';' + 'University' + ';' + 'Country' + ';' + 'Score' + '\n')
        f.close()
    main()

    df = pd.read_csv('qs-rank.txt', delimiter=';', header=None)
    df.to_csv('qs-rank.csv', index=False)

    print('Done & Convered to CSV')