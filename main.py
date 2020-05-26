
# ? robots.txtの表示…hpのurlの末尾に/robots.txt
# ? User-agent　：Disallow になっているPathは、アクセス禁止

import requests

sach = {'area': 'kansai', 'howto': '', 'fish': 'fish-akou', 'tackle': ''}
url = 'https://fishing.ne.jp/'
req = requests.get(url, params=sach, timeout=15)

with open('sample,htm', 'W', encoding='utf-8') as f:
    f.write(req.text)
