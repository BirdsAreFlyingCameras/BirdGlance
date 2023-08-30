import requests
import socket as s
import json
from urllib.parse import urlparse
from dns.resolver import *

def Main():

    SpecialCharacters = [
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
        '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^',
        '_', '`', '{', '|', '}', '~'
    ]

    URL = input("Website URL: ")  # Takes the url that will be used in the search's

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

            def IsURLAnIP():
                global IsURLAnIPOutput

                try:
                    s.inet_aton(URL)
                    IsURLAnIPOutput = True
                    if IsURLAnIPOutput == True:
                        print("URL is an IP address")
                except s.error:
                    IsURLAnIPOutput = False
                    if IsURLAnIPOutput == False:
                        print("URL is not an IP address")

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
                        URLHTTP = "http://" + URL
                        URLHTTPS = "https://" + URL

                for i in TLDS:
                    if URL.endswith("/"):
                        URL = URL[:-1]
                    if URL.endswith(i):
                        TLDSValid = True
                        print("URL has a valid TLDS (.com,.org, etc.)")
                        break

                if TLDSValid is False:
                    input("URL does not have a valid TLDS Do you want to continue? [Y/N] ")
                    if input == "y" or "Y":
                        print("Continuing...")
                    else:
                        print("Exiting...")
                        exit()

            refactor(URL)  # Calls the refactor function with the parameter URL

            def Checks():

                def HTTPcheck():

                    global HTTPValid

                    GetReqStatus = requests.get(url=URLHTTP)

                    if GetReqStatus.status_code == 200:
                        print(URLHTTP + " returned status code 200")

                        HTTPValid = True

                    else:
                        print(f"{URL} is not a valid URL")

                        HTTPValid = False

                def HTTPScheck():

                    global HTTPSValid

                    getreqstatus = requests.get(url=URLHTTPS)

                    if getreqstatus.status_code == 200:
                        print(URLHTTPS + " returned status code 200")

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
                    print("Hostname:" + HostnameForIP)
                    print("IP Address: " + WebSiteIP)
                    print("ISP:" + IPinfoISPOutput)
                    print("Country:" + IPinfoCountryOutput)
                    print("State or Region:" + IPinfoStateOrRegionOutput)
                    print("City:" + IPinfoCityOutput)

                InfoOutput()

                def InfoOutputTXT():
                    HOSTNAMEFORTXT = HostnameForIP.replace("www.", "").replace(".com", "")

                    output = [

                        "Hostname: " + HostnameForIP, "\n",
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

    BasicInfo()

Main()
