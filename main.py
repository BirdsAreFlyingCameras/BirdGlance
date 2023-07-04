import requests
import socket as s
import json
from urllib.parse import urlparse


def WebsiteInput():
    URL = input("Website URL: ")  # Takes the url that will be used in the search's

    def refactor(URL):

        global URLHTTPS, URLHTTP

        if URL.startswith('https://') or URL.startswith('http://'):
            URLHTTPS = URL
            URLHTTP = URL
        else:
            URLHTTPS = "https://" + URL
            URLHTTP = "http://" + URL

    refactor(URL)

    def Checks():

        def HTTPcheck():

            global HTTPValid

            getreqstatus = requests.get(url=URLHTTP)

            if getreqstatus.status_code == 200:
                print(URLHTTP + " is valid")

                HTTPValid = True

            else:
                print("URL is not valid")

                HTTPValid = False

        def HTTPScheck():

            global HTTPSValid

            getreqstatus = requests.get(url=URLHTTPS)

            if getreqstatus.status_code == 200:
                print(URLHTTPS + " is valid")

                HTTPSValid = True



            else:
                print("URL is not valid")

                HTTPSValid = False

        HTTPcheck()
        HTTPScheck()

    Checks()

    def GetHostName():

        global HOSTNAMEFORIP

        o = urlparse(URLHTTP)

        HOSTNAMEFORIP = o.hostname

        print(HOSTNAMEFORIP)

    GetHostName()

    def GetWebsiteIP():

        global WebSiteIP

        WebSiteIP = s.gethostbyname(HOSTNAMEFORIP)

    GetWebsiteIP()

    def GetWebsiteIPInfo():

        def Country():
            global IPinfoCountry

            GetIpInfoCountry = requests.get(url="http://ip-api.com/json/" + WebSiteIP + "?fields=1")

            IPinfoCountry = json.loads(GetIpInfoCountry.text)
            IPinfoCountry = json.dumps(IPinfoCountry)


        Country()

        def StateOrRegion():
            global IPinfoStateOrRegion

            GetIpInfoStateOrRegion = requests.get(url="http://ip-api.com/json/" + WebSiteIP + "?fields=8")

            IPinfoStateOrRegion = json.loads(GetIpInfoStateOrRegion.text)
            IPinfoStateOrRegion = json.dumps(IPinfoStateOrRegion)


        StateOrRegion()

        def City():
            global IPinfoCity

            GetIpInfoCity = requests.get(url="http://ip-api.com/json/" + WebSiteIP + "?fields=16")

            IPinfoCity = json.loads(GetIpInfoCity.text)
            IPinfoCity = json.dumps(IPinfoCity)


        City()

        def ISP():
            global IPinfoISP

            GetIPinfoISP = requests.get(url="http://ip-api.com/json/" + WebSiteIP + "?fields=512")

            IPinfoISP = json.loads(GetIPinfoISP.text)

            IPinfoISP = json.dumps(IPinfoISP)


        ISP()

        def InfoOutput():

            print(IPinfoCountry)
            print(IPinfoStateOrRegion)
            print(IPinfoCity)
            print(IPinfoISP)

        InfoOutput()

    GetWebsiteIPInfo()


WebsiteInput()
