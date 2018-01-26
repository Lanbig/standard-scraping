# Author : Ben Rodrawangpai
# Date 1/25/2018

import requests
import csv
from bs4 import BeautifulSoup
import time


def extract_meta_refresh(soup):
    # parameter[s]: soup-object
    # output: meta-refresh-url-string

    element = soup.find('meta', attrs={'http-equiv': 'refresh'})
    refresh_content = element['content']
    return(refresh_content.partition('=')[2])


# Configuration
url = "http://www.iec.ch/members/"
base_url = 'http://www.iec.ch'
filename = 'data/iec_member_data_' + time.strftime("%Y%m%d-%H%M%S") + '.csv'
debug_mode = 0

if __name__ == "__main__":
    # Scrape member page
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    meta_refresh = extract_meta_refresh(soup)  # extract meta-refresh

    # Scrape [actual] member page
    re_page = requests.get(base_url + meta_refresh)
    soup = BeautifulSoup(re_page.text, "html.parser")

    # Scrape member table
    member_table = soup.find('table', attrs={'class': 'dashlist'})

    # scrape data and write to CSV
    member_data = open(filename, 'w')
    writer = csv.writer(member_data, delimiter=',')
    writer.writerow(['country', 'membership', 'p_member', 'o_member'])

    for tr in member_table.find_all('tr')[1:]:
        tds = tr.find_all('td')

        if debug_mode:
            print(str(tds[0].text).strip(), str(tds[2].text).strip(), str(tds[4].text).strip(), str(tds[5].text).strip())

        writer.writerow([str(tds[0].text).strip(), str(tds[2].text).strip(), str(tds[4].text).strip(), str(tds[5].text).strip()])