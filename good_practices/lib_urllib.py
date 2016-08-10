import urllib.request
# this is for python3:
from bs4 import BeautifulSoup

# HTTP File Download
urllib.request.urlretrieve('https://framasoft.org/accueil/img/pingouinVolantRefait.png',
                           'pic.png')

# Retrieve an HTML
with urllib.request.urlopen('http://python.org/') as response:
    html = response.read()

# Find a div (TO IMPROVE, at least the example)
    soup = BeautifulSoup(html, "lxml")
#    print(soup.body.find('div', attrs={'id':'oldie-warning'}).text)
