import hashlib
import logging as log
from contextlib import closing
from urllib.request import urlopen, urlretrieve
from functools import partial

log.basicConfig(level=log.DEBUG)


data = [
    ('../data/TAIR10_pep_20101214_updated.txt', 'http://www.arabidopsis.org/download_files/Sequences/TAIR10_blastsets/TAIR10_pep_20101214_updated'),
    
]


def md5sum(fhand, bufsize=10):
    """Return the md5 hash of a file"""

    log.debug('Computing md5sum...')
    m = hashlib.md5()
    for buf in iter(partial(fhand.read, bufsize), b''):
            m.update(buf)

    return m.hexdigest()


def get_remote_md5sum(url):
    with closing(urlopen(url)) as u:
        return md5sum(u)

    
def get_remote_file(url, outfile):
    urlretrieve(url, outfile)

    
def check_for_updates(fhand, url):

    md5_loc = md5sum(fhand)
    log.info('md5sum for {0}: {1}'.format(fhand.name, md5_loc))
    md5_rem = get_remote_md5sum(url)
    log.info('md5sum for {0}: {1}'.format(url, md5_rem))

    if md5_loc != md5_rem:
        log.info('Local version of "{}" appears outdated... \
Downloading newer version... '.format(fhand.name))

        get_remote_file(url, fhand.name)

    else:
        log.info('Local version of "{}" appears up to date... \
Doing nothing more.'.format(fhand.name))
        
    
if __name__ == '__main__':

    for d in data:
        check_for_updates(open(d[0], 'rb'), d[1])
    
