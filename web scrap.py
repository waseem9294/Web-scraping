import requests , bs4

url = 'https://webscraper.io/blog'

req = requests.get(url, timeout=5)
html = req.text
soup = bs4.BeautifulSoup(html , 'html.parser')
para = soup.find_all('img', class_='img-responsive')

# for p in para:
#     print(p.get_text())
img_url = [i.get('src') for i in para]

for index, url in enumerate(img_url):
    imgs = requests.get(url, timeout=5)
    with open(f'img-{index}.png','wb') as f:
        f.write(imgs.content)
        