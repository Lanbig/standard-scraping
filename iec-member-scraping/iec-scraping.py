# Author : Ben Rodrawangpai
# Date 1/25/2018

import requests
import csv
from bs4 import BeautifulSoup
import time

# Configuration
url = "http://www.iec.ch/members/"
filename = 'data/iso_member_data_' + time.strftime("%Y%m%d-%H%M%S") + '.csv'
debug_mode = 0

# Scrape member page
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

# need to handle Meta refresh

# Scrape member table
member_table = soup.find('div', attrs={'id': 'DASHBOARD_NCLIST'})