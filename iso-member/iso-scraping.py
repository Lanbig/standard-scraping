# Author : Ben Rodrawangpai
# Date 1/25/2018

import requests
import csv
from bs4 import BeautifulSoup
import time

# Configuration
url = "https://www.iso.org/members.html"
filename = 'data/iso_member_data_' + time.strftime("%Y%m%d-%H%M%S") + '.csv'
debug_mode = 0

if __name__ == "__main__":
    # Scrape member page
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    # Scrape member table
    member_table = soup.find('table', attrs={'id': 'datatable-members'})

    # scrape data and write to CSV
    member_data = open(filename, 'w')
    writer = csv.writer(member_data, delimiter=',')
    writer.writerow(['country', 'membership', 'tc_participation', 'pdc_participation'])

    with member_data:
        for tr in member_table.find_all('tr')[1:]:
            tds = tr.find_all('td')

            if debug_mode:
                print(tds[0].text, tds[2].text, tds[3].text, tds[4].text)

            writer.writerow([tds[0].text, tds[2].text, tds[3].text, tds[4].text])