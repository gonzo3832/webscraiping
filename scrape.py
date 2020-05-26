import requests
import bs4
import csv
import bs4

# ? sach={'q':'Python', 'users':'1000'}
# ? url = 'http://b.hatena.ne.jp/search/text'
# ? req = requests.get(url, params = sach, timeout = 15)

filename = 'testpage.html'
testpage_html = open(filename,'r',encoding="utf-8")
soup = bs4.BeautifulSoup(testpage_html, 'html.parser')


bookmarks = []

for b in soup.findAll('section', {'class':'fishingpost-child-box cl  tax2'}):
    #title = b.find('a').get('title')
    url = b.find('a').get('href')
    bookmarks.append([url])
    #bookmarks.append([title, url])

# ? with open('bookmarks.csv', 'w', encoding='shift-jis') as f:
with open('bookmarks.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(bookmarks)