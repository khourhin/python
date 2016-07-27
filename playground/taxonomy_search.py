#! /usr/bin/python
from Bio import Entrez


def get_taxonomy(query):

    Entrez.email = "ekornobis@gmail.com"

    # Get data from NCBI
    handle = Entrez.esearch(db="Taxonomy", term=query)
    record = Entrez.read(handle)

    # Get NCBI id of the taxa and its data
    id = record["IdList"][0]

    handle = Entrez.efetch(db="Taxonomy", id=id, retmode="xml")
    records = Entrez.read(handle)

    # Print each taxonomy entries:
    for lineage in records[0]["LineageEx"]:
        print "{0}:\t\t {1}".format(lineage["Rank"], lineage["ScientificName"])


def get_web_info(query):
    webbrowser.open("http://en.wikipedia.org/wiki/{0}".format(query))
    uicn_query = query.strip().replace(" ", "%20")
    webbrowser.open(
        "http://www.iucnredlist.org/search?text={0}".format(uicn_query))

#-------------------------------------------------------------------------------
# The Main
#-------------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse
    import webbrowser

    parser = argparse.ArgumentParser(description="Application for Biology")
    parser.add_argument("-t", "--tax_query", type=str)
    parser.add_argument("-w", "--web_info", action='store_true')
    args = parser.parse_args()

    if args.tax_query:
        get_taxonomy(args.tax_query)

        if args.web_info:
            get_web_info(args.tax_query)
