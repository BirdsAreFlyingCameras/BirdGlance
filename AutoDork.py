import requests
from googlesearch import search
import urllib
from bs4 import BeautifulSoup
from collections import *


class MethodsClass:
    # (Filter, Description, Example)

    # Define the SearchFilter namedtuple
    SearchFilter = namedtuple('SearchFilter', ['Filter', 'Description', 'Example'])

    # Create instances of the SearchFilter namedtuple for each search filter
    allintext = SearchFilter(
        Filter='allintext',
        Description='Searches for occurrences of all the keywords given.',
        Example='allintext:"keyword"'
    )

    intext = SearchFilter(
        Filter='intext',
        Description='Searches for the occurrences of keywords all at once or one at a time.',
        Example='intext:"keyword"'
    )

    inurl = SearchFilter(
        Filter='inurl',
        Description='Searches for a URL matching all the keywords in the query.',
        Example='inurl:"keyword"'
    )

    allinurl = SearchFilter(
        Filter='allinurl',
        Description='Searches for a URL matching all the keywords in the query.',
        Example='allinurl:"keyword"'
    )

    intitle = SearchFilter(
        Filter='intitle',
        Description='Searches for occurrences of keywords in title all or one.',
        Example='intitle:"keyword"'
    )

    allintitle = SearchFilter(
        Filter='allintitle',
        Description='Searches for occurrences of keywords all at a time.',
        Example='allintitle:"keyword"'
    )

    site = SearchFilter(
        Filter='site',
        Description='Specifically searches that particular site and lists all the results for that site.',
        Example='site:"www.google.com"'
    )

    filetype = SearchFilter(
        Filter='filetype',
        Description='Searches for a particular filetype mentioned in the query.',
        Example='filetype:"pdf"'
    )

    link = SearchFilter(
        Filter='link',
        Description='Searches for external links to pages.',
        Example='link:"keyword"'
    )

    numrange = SearchFilter(
        Filter='numrange',
        Description='Used to locate specific numbers in your searches.',
        Example='numrange:321-325'
    )

    beforeafter = SearchFilter(
        Filter='before/after',
        Description='Used to search within a particular date range.',
        Example='filetype:pdf & (before:2000-01-01 after:2001-01-01)'
    )

    allinanchor = SearchFilter(
        Filter='allinanchor (and also inanchor)',
        Description='This shows sites which have the key terms in links pointing to them, in order of the most links.',
        Example='inanchor:rat'
    )

    allinpostauthor = SearchFilter(
        Filter='allinpostauthor (and also inpostauthor)',
        Description='Exclusive to blog search, this one picks out blog posts that are written by specific individuals.',
        Example='allinpostauthor:"keyword"'
    )

    related = SearchFilter(
        Filter='related',
        Description='List web pages that are “similar” to a specified web page.',
        Example='related:www.google.com'
    )

    # Example usage:
    print(allintext.Example)




class CommonCombos:

    CommonCombosTemp = namedtuple('CommonCombos', ['Filter',  'input'])



#
#URL = "https://www.goldlawcorp.com/contact/"
#test = requests.get(URL)
#print(test.text)
#
for url in search('https://www.goldlawcorp.com/contact/'):
   print(url)


"""
site:"https://www.example.com" intext:"email"
site:"https://www.example.com" intext:"admin"





"""