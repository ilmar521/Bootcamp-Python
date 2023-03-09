import requests
import time

list_of_sites = [
    'https://www.google.com',
    'https://www.imdb.com',
    'https://www.ynet.co.il'
]


def main():
    results = {}
    for site in list_of_sites:
        t1 = time.time()
        response = requests.get(site)
        t2 = time.time()
        results[site] = t2 - t1

    print('Results of time analyzing:')
    for key, value in results.items():
        print(f'{key} took {value} s.')


main()
