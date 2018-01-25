# Standard Scraping Tool

[![License: ODbL](https://img.shields.io/badge/License-ODbL-brightgreen.svg)](https://opendatacommons.org/licenses/odbl/)


Standard Scraping Tool is a python script designed to pulling data out of HTML format. The script will read the data-country-
member from IEC and ISO official webpage. The data is used for Code and Standard indicator and they are published on 
ULSafetyIndex.org. The script was developed using Python, BeautifulSoup.


## Data Fields
### 1. ISO Members 

Country | Detail
------------ | -------------
country | Country
membership | Types of membership
tc_participation | Technical commitee
pdc_participation | Errr X#$%@&!#^%

*URL: https://www.iso.org/members.html*


### 2. IEC Members 

Country | Detail
------------ | -------------
membership | Types of membership
p_member | Number of Participating Member
o_member | Number of Observer Member

*URL: http://www.iec.ch/members/ (Meta refresh)*
