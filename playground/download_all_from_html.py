#! /usr/bin/python3

from bs4 import BeautifulSoup
import urllib
import os.path

#-------------------------------------------------------------------------------
def get_html(url):
    """
    From an url, return a html string
    """
    
    html = urllib.request.urlopen(url).read()
    return html

#-------------------------------------------------------------------------------
def find_links_to_type(ext, html):
    """
    Find the html links '<a>' with the required extension
    Return a list of tuples (link url, filename for copy)
    """
    
    soup = BeautifulSoup(html, 'lxml')
    res = [ (link.get('href'), link.get('download')) for link in soup.find_all('a') ]
    print(res)
    res = [ link for link in res if link[0].endswith(ext)]
    return res

#-------------------------------------------------------------------------------
def download_links(links, ext):
    """
    From the list of tuples from 'find_links_to_type', download the links.
    """
    
    for link in links:
        url = link[0]
        filename = link[1].replace('/','-') + ext
        filename = ' '.join(filename.split())
        if os.path.exists(filename):
            print('Already downloaded %s' % filename )
            continue
        print('Downloading %s' % filename )
        urllib.request.urlretrieve(url, filename )

#-------------------------------------------------------------------------------
if __name__ == '__main__':
        
    url = 'http://www.clementgrimal.fr/darwin/'
    ext = '.mp3'
    url = 'http://www.richmolnar.com/Sounds/'
    ext = '.wav'
    html = get_html(url)
    links = find_links_to_type(ext, html)
    print(links)
    download_links(links, ext)
