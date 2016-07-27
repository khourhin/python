#! /usr/bin/env python

import sys
import os
import urllib3
import json
import csv
import re

def getMovieList(folder):

    films_l = os.listdir(folder)
    # remove parenthesis present in title of folder
    films_l = [ re.sub("\(.*?\)", "", i ).strip() for i in films_l ]
    return films_l 

def getUrlData(films_l):

    with open("the_film_list.csv", "wb") as f:
        for film in films_l:
            url = "http://www.imdbapi.com/?t=" + film.replace(" ", "+")
            request = urllib2.Request(url)
            response = json.load(urllib2.urlopen(request))
            # For some reason the [key] syntax is not working
            title = response.get("Title")
            date = response.get("Year").encode("utf-8")
            language = response.get("Language")
            director = response.get("Director")
            genre = response.get("Genre")
            runtime = response.get("Runtime")
            imdbID = response.get("imdbID")
            
            writer = csv.writer(f, delimiter=",")
            link = '=HYPERLINK("http://www.imdb.com/title/%s"' % imdbID
            writer.writerow([title, date, director, language, runtime,
                             genre, link])
            
# MAIN
#-------------------------------------------------------------------------------

if __name__ == "__main__":

    movie_l = getMovieList(sys.argv[1])
    getUrlData(movie_l)
