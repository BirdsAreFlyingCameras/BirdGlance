import requests
import socket as s
import json
from urllib.parse import urlparse
from dns.resolver import *
import sys

from colorama import init, Fore, Back, Style

from PyEnhance import Stamps

Stamp = Stamps.Stamp

Input = Stamp.Input
Output = Stamp.Output
Error = Stamp.Error
Info = Stamp.Info
Warn = Stamp.Warn

PostiveStatusCodes = [200, 301, 401, 403]

def Main():

    global URL


    SpecialCharacters = [
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
        '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^',
        '_', '`', '{', '|', '}', '~'
    ]

    URL = input(f"{Input} Website URL: ")  # Takes the url that will be used in the search's
    print('\n')
    def BasicInfo():
        def Stage1():
            def FetchTLDS():

                global TLDSs
                global TLDS


                TLDSs = "https://data.iana.org/TLD/tlds-alpha-by-domain.txt"
                response = requests.get(TLDSs)
                response.raise_for_status()

                # The file uses line breaks for each TLD, and we filter out comments which start with '#'
                TLDS = [line.strip().lower() for line in response.text.splitlines() if not line.startswith('#')]

            FetchTLDS()
            def CheckTLDS():
                global TLDSValid
                global URL
                TLDSValid = False
                for i in TLDS:
                    if URL.endswith("/"):
                        URL = URL[:-1]
                    if URL.endswith(i):
                        TLDSValid = True
                        print(f"{Info} URL has a valid TLDS (.com, .org, .xyz, etc.)")
                        break

                if TLDSValid is False:
                    input(f"{Error} URL does not have a valid TLDS Do you want to continue? [Y/N] ")
                    if input == "y" or "Y":
                        print("Continuing...")
                    else:
                        print("Exiting...")
                        sys.exit()
            CheckTLDS()
            def IsURLAnIP():
                global IsURLAnIPOutput

                try:
                    s.inet_aton(URL)
                    IsURLAnIPOutput = True
                    if IsURLAnIPOutput == True:
                        print(f"{Info} URL is an IP address")
                except s.error:
                    IsURLAnIPOutput = False
                    if IsURLAnIPOutput == False:
                        print(f"{Info} URL is not an IP address")

            IsURLAnIP()

            def refactor(URL):  # defines the refactor function and passes the URL variable as a parameter
                global URLHTTPS, URLHTTP  # Sets the variables URL HTTPS and URL HTTP to global variables meaning they can be called outside of this function.
                global TLDSValid
                TLDSValid = False


                for i in "https://", "http://":
                    if URL.startswith(i):
                        if i == "https://":
                            URLHTTPS = URL
                            URLHTTP = URL.replace("https://", "http://")
                        if i == "http//":
                            URLHTTP = URL
                            URLHTTPS = URL.replace("http://", "https://")
                        break
                    else:
                        URLHTTP = f"http://{URL}"
                        URLHTTPS = f"https://{URL}"



            refactor(URL)  # Calls the refactor function with the parameter URL

            def Checks():

                def HTTPcheck():

                    global HTTPValid

                    GetReqStatus = requests.get(url=URLHTTP)

                    if GetReqStatus.status_code in PostiveStatusCodes:
                        print(f"{Info} HTTP Valid")

                        HTTPValid = True

                    else:
                        print(f"{URL} is not a valid URL")

                        HTTPValid = False

                def HTTPScheck():

                    global HTTPSValid

                    getreqstatus = requests.get(url=URLHTTPS)

                    if getreqstatus.status_code == 200:
                        print(f"{Info} HTTPS Valid")

                        HTTPSValid = True

                    else:
                        print(f"{URL} is not a valid URL")

                        HTTPSValid = False

                HTTPcheck()
                HTTPScheck()

            Checks()

        Stage1()

        def Stage2():

            def GetHostName():
                global HostnameForIP

                o = urlparse(URLHTTP)
                HostnameForIP = o.hostname

            GetHostName()

            def GetWebSiteIP():
                global WebSiteIP

                WebSiteIP = s.gethostbyname(HostnameForIP)

            GetWebSiteIP()


        Stage2()

        def Stage3():
            def GetWebsiteIPInfo():
                global Replace
                def Country():
                    global IPinfoCountry
                    global IPinfoCountryOutput

                    URL = f'http://ip-api.com/json/{WebSiteIP}?fields=1'

                    GetIpInfoCountry = requests.get(url=URL)

                    IPinfoCountry = json.loads(GetIpInfoCountry.text)
                    IPinfoCountry = json.dumps(IPinfoCountry)

                    IPinfoCountryOutput = (IPinfoCountry.replace("{", "").replace("}", "")
                                           .replace(":", "").replace("country", "")
                                           .replace('"', ""))
#
                Country()

                def StateOrRegion():
                    global IPinfoStateOrRegion
                    global IPinfoStateOrRegionOutput

                    URL = f'http://ip-api.com/json/{WebSiteIP}?fields=8'

                    GetIpInfoStateOrRegion = requests.get(url=URL)

                    IPinfoStateOrRegion = json.loads(GetIpInfoStateOrRegion.text)
                    IPinfoStateOrRegion = json.dumps(IPinfoStateOrRegion)

                    IPinfoStateOrRegionOutput = IPinfoStateOrRegion.replace("{", "").replace("}", "").replace(":", "") \
                        .replace("regionName", "").replace('"', "")

                StateOrRegion()

                def City():
                    global IPinfoCity
                    global IPinfoCityOutput

                    URL = f'http://ip-api.com/json/{WebSiteIP}?fields=16'

                    GetIpInfoCity = requests.get(url=URL)

                    IPinfoCity = json.loads(GetIpInfoCity.text)
                    IPinfoCity = json.dumps(IPinfoCity)

                    IPinfoCityOutput = IPinfoCity.replace("{", "").replace("}", "").replace(":", "") \
                        .replace("city", "").replace('"', "")

                City()

                def ISP():
                    global IPinfoISP
                    global IPinfoISPOutput

                    URL = f'http://ip-api.com/json/{WebSiteIP}?fields=512'

                    GetIPinfoISP = requests.get(url=URL)

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
                    global Info, Warn, Output, Input, Error
                    print('\n')
                    print(f"{Output} Hostname: {HostnameForIP}")
                    print(f"{Output} IP Address: {WebSiteIP}")
                    print(f"{Output} ISP:{IPinfoISPOutput}")
                    print(f"{Output} Country:{IPinfoCountryOutput}")
                    print(f"{Output} State or Region:{IPinfoStateOrRegionOutput}")
                    print(f"{Output} City:{IPinfoCityOutput}")

                InfoOutput()

                def InfoOutputTXT():
                    HOSTNAMEFORTXT = HostnameForIP.replace("www.", "").replace(".com", "")

                    output = [

                        f"Hostname: {HostnameForIP} \n",
                        f"IP Address: {WebSiteIP} \n",
                        f"ISP:{IPinfoISPOutput} \n",
                        f"Country:{IPinfoCountryOutput} \n",
                        f"State or Region:{IPinfoStateOrRegionOutput}\n",
                        f"City:{IPinfoCityOutput}\n"
                    ]

                    with open(f"{HOSTNAMEFORTXT}.txt", 'w') as file:
                        file.writelines(output)

                InfoOutputTXT()

            Output()

        Stage4()

    BasicInfo()

Main()


# WebsiteInfoGraber Beta 1.1
# Gets basic Info from a website URL


# Not A Bird
# CEO of Bird Inc.