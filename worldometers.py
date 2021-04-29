import csv, requests, bs4

url = 'https://www.worldometers.info/world-population/population-by-country/'

req = requests.get(url , timeout=5)
html = req.text
soup = bs4.BeautifulSoup(html , 'html.parser')


with open('worldometers.csv','w') as f:

    for tr in soup.find_all('tr'):
        data=[]

        for th in tr.find_all('th'):
            data.append(th.text)
        
        for td in tr.find_all('td'):
            data.append(td.text)

        csv_writer = csv.writer(f)
        csv_writer.writerow(data)
