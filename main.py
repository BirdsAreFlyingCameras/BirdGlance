import requests
import socket as s
import json
from urllib.parse import urlparse


def Main():
    URL = input("Website URL: ")  # Takes the url that will be used in the search's

    def Stage1():
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
                    print(URLHTTP + " returned status code 200")

                    HTTPValid = True

                else:
                    print("URL is not valid")

                    HTTPValid = False

            def HTTPScheck():

                global HTTPSValid

                getreqstatus = requests.get(url=URLHTTPS)

                if getreqstatus.status_code == 200:
                    print(URLHTTPS + " returned status code 200")

                    HTTPSValid = True



                else:
                    print("URL is not valid")

                    HTTPSValid = False

            HTTPcheck()
            HTTPScheck()

        Checks()

    Stage1()

    def Stage2():

        def GetHostName():

            global HOSTNAMEFORIP

            o = urlparse(URLHTTP)

            HOSTNAMEFORIP = o.hostname

        GetHostName()

        def GetWebSiteIP():

            global WebSiteIP

            WebSiteIP = s.gethostbyname(HOSTNAMEFORIP)

        GetWebSiteIP()

    Stage2()

    def Stage3():
        def GetWebsiteIPInfo():
            def Country():
                global IPinfoCountry
                global IPinfoCountryOutput

                GetIpInfoCountry = requests.get(url="http://ip-api.com/json/" + WebSiteIP + "?fields=1")

                IPinfoCountry = json.loads(GetIpInfoCountry.text)
                IPinfoCountry = json.dumps(IPinfoCountry)

                IPinfoCountryOutput = IPinfoCountry.replace("{", "").replace("}", "").replace(":", "") \
                    .replace("country", "").replace('"', "")

            Country()

            def StateOrRegion():
                global IPinfoStateOrRegion
                global IPinfoStateOrRegionOutput

                GetIpInfoStateOrRegion = requests.get(url="http://ip-api.com/json/" + WebSiteIP + "?fields=8")

                IPinfoStateOrRegion = json.loads(GetIpInfoStateOrRegion.text)
                IPinfoStateOrRegion = json.dumps(IPinfoStateOrRegion)

                IPinfoStateOrRegionOutput = IPinfoStateOrRegion.replace("{", "").replace("}", "").replace(":", "") \
                    .replace("regionName", "").replace('"', "")

            StateOrRegion()

            def City():
                global IPinfoCity
                global IPinfoCityOutput

                GetIpInfoCity = requests.get(url="http://ip-api.com/json/" + WebSiteIP + "?fields=16")

                IPinfoCity = json.loads(GetIpInfoCity.text)
                IPinfoCity = json.dumps(IPinfoCity)

                IPinfoCityOutput = IPinfoCity.replace("{", "").replace("}", "").replace(":", "") \
                    .replace("city", "").replace('"', "")

            City()

            def ISP():
                global IPinfoISP
                global IPinfoISPOutput

                GetIPinfoISP = requests.get(url="http://ip-api.com/json/" + WebSiteIP + "?fields=512")

                IPinfoISP = json.loads(GetIPinfoISP.text)
                IPinfoISP = json.dumps(IPinfoISP)

                IPinfoISPOutput = IPinfoISP.replace("{", "").replace("}", "").replace(":", "") \
                    .replace("isp", "").replace('"', "")

            ISP()

        GetWebsiteIPInfo()

    Stage3()

    def Stage4():
        def Output():
            def InfoOutput():
                print("Hostname:" + HOSTNAMEFORIP)
                print("IP Address: " + WebSiteIP)
                print("ISP:" + IPinfoISPOutput)
                print("Country:" + IPinfoCountryOutput)
                print("State or Region:" + IPinfoStateOrRegionOutput)
                print("City:" + IPinfoCityOutput)

            InfoOutput()

            def InfoOutputTXT():
                HOSTNAMEFORTXT = HOSTNAMEFORIP.replace("www.", "").replace(".com", "")

                output = [

                    "Hostname: " + HOSTNAMEFORIP, "\n",
                    "IP Address: " + WebSiteIP, "\n",
                    "ISP:" + IPinfoISPOutput, "\n",
                    "Country:" + IPinfoCountryOutput, "\n",
                    "State or Region:" + IPinfoStateOrRegionOutput, "\n",
                    "City:" + IPinfoCityOutput, "\n"
                ]

                with open(HOSTNAMEFORTXT + '.txt', 'w') as file:
                    file.writelines(output)

            InfoOutputTXT()

        Output()

    Stage4()


Main()
