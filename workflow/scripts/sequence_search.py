import json
import logging
import requests
import data_downloader
import sys


logging.basicConfig(level=logging.INFO,
                    # filename='data_downloader.log',
                    format='%(asctime)s %(levelname)s %(message)s',
                    )


def ncbi_search(country, limit):
    """
    A script to perform an NCBI sequence search

    :param country:
    :param limit:
    :return:
    """
    ncbi_baseurl = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

    # declare default parameters
    params = {'db': 'nuccore', 'term': f"HIV-1[Organism] AND {country}[Title Word] full",
              'retmode': 'json', 'rettype': 'json', 'retmax': limit, 'usehistory': 'y'}

    # Send a request to the ncbi
    try:
        logging.info('Searching ncbi')
        handles = requests.post(ncbi_baseurl, data=params)
        logging.info('Search successful')
        print("webenv", json.loads(handles.text)['esearchresult']['webenv'])
        id_lists = json.loads(handles.text)['esearchresult']['idlist']
        data_downloader.query_ncbi(id_lists, json.loads(handles.text)['esearchresult']['webenv'])

    except Exception as e:
        logging.error('An error occurred', e)

    pass


if __name__ == '__main__':
    if len(sys.argv) > 2:
        ncbi_search(sys.argv[1], int(sys.argv[2]))
    else:
        logging.error("Please input country of the isolate and the limit of the sequences to be returned \n"
                      "\nuse this format:$ python3 sequence_search.py <county> <limit number> \n")

