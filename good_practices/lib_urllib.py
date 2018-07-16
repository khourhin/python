import urllib.request
# this is for python3:
from bs4 import BeautifulSoup


def test1():

    # HTTP File Download
    urllib.request.urlretrieve('https://framasoft.org/accueil/img/pingouinVolantRefait.png',
                               'pic.png')

    # Retrieve an HTML
    with urllib.request.urlopen('http://python.org/') as response:
        html = response.read()

        # Find a div (TO IMPROVE, at least the example)
        soup = BeautifulSoup(html, "lxml")
        #    print(soup.body.find('div', attrs={'id':'oldie-warning'}).text)


def with_auth():

    # create a password manager
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

    # Add the username and password.
    # If we knew the realm, we could use it instead of None.
    top_level_url = "https://c3bi.pasteur.fr/hub/projects/"
    username = 'ekornobi'
    password = 'perceval#PASFAUX42'

    password_mgr.add_password(None, top_level_url, username, password)

    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib.request.build_opener(handler)

    # use the opener to fetch a URL
    opener.open('https://c3bi.pasteur.fr/hub/projects/?projects=table')

    # Install the opener.
    # Now all calls to urllib.request.urlopen use our opener.
    urllib.request.install_opener(opener)

    with urllib.request.urlopen('https://c3bi.pasteur.fr/hub/projects/?projects=table') as response:
        html = response.read()
        print(html)


with_auth()
