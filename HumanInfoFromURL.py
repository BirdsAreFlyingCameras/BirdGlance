import requests
from bs4 import BeautifulSoup

import re

URL = "https://brandaffair.ro/contact"

webpage = requests.get(URL)

soup = BeautifulSoup(webpage.text, 'html.parser')

SoupOutput = (soup.text)

strings = '+1234578914'

pattern = r"\b\d{3}\d{3}\d{4}\b"

PhoneNumbers = re.finditer(pattern, SoupOutput)

print(PhoneNumbers)


"""
The four things im looking for in the soup output are:

1. Names of the people who work at the company

2. Emails of the people who work at the company

3. Phone numbers of the people who work at the company

4. The company's address

"""