import socket
import threading as t
import colorama
import time


start_time = time.time()
host = "google.com"


class colors:
    colorama.init()
    print(colorama.Fore.RED)
    print(colorama.Style.BRIGHT)


class ListsAndDicts:
    global OpenPortsList
    global CommonPortsList
    global CommonPortOutputList
    global UnknownPortOutputList
    global OpenPortsListFilteredAndDone
    CommonPortOutputList = []
    UnknownPortOutputList = []
    OpenPortsList = []
    OpenPortsListFilteredAndDone = []
    CommonPortsList = {
        1: 'TCPMUX',
        5: 'RJE',
        7: 'ECHO',
        9: 'DISCARD',
        11: 'SYSTAT',
        13: 'DAYTIME',
        17: 'QOTD',
        18: 'MSP',
        19: 'CHARGEN',
        20: 'FTP_DATA',
        21: 'FTP_CONTROL',
        22: 'SSH',
        23: 'TELNET',
        25: 'SMTP',
        37: 'TIME',
        42: 'NAMESERVER',
        43: 'WHOIS',
        49: 'TACACS',
        53: 'DNS',
        67: 'DHCP_CLIENT',
        68: 'DHCP_SERVER',
        69: 'TFTP',
        70: 'Gopher',
        79: 'Finger',
        80: 'HTTP',
        88: 'Kerberos',
        102: 'MS Exchange',
        110: 'POP3',
        113: 'IDENT',
        119: 'NNTP',
        123: 'NTP',
        135: 'RPC',
        137: 'NetBIOS-NS',
        138: 'NetBIOS-DGM',
        139: 'NetBIOS-SSN',
        143: 'IMAP',
        161: 'SNMP',
        179: 'BGP',
        194: 'IRC',
        201: 'AppleTalk',
        220: 'IMAP3',
        389: 'LDAP',
        443: 'HTTPS',
        445: 'SMB',
        464: 'Kerberos Change/Set password',
        465: 'SMTPS',
        500: 'ISAKMP',
        514: 'Syslog',
        520: 'RIP',
        530: 'RPC',
        543: 'Kerberos (klogin)',
        544: 'Kerberos (kshell)',
        546: 'DHCPv6 Client',
        547: 'DHCPv6 Server',
        554: 'RTSP',
        587: 'SMTP (Message Submission)',
        631: 'Internet Printing Protocol (IPP)',
        636: 'LDAPS',
        873: 'rsync',
        902: 'VMware Server Console',
        989: 'FTPS (data)',
        990: 'FTPS (control)',
        993: 'IMAPS',
        995: 'POP3S',
        1025: 'Microsoft RPC',
        1433: 'Microsoft SQL Server',
        1434: 'Microsoft SQL Monitor',
        1521: 'Oracle database default listener',
        1723: 'PPTP',
        1724: 'PPTP',
        2049: 'NFS',
        2082: 'cPanel',
        2083: 'cPanel',
        2181: 'ZooKeeper',
        2222: 'DirectAdmin',
        3306: 'MySQL',
        3389: 'RDP',
        3690: 'SVN',
        4333: 'mSQL',
        4444: 'Metasploit',
        5060: 'SIP',
        5432: 'PostgreSQL',
        5900: 'VNC',
        5984: 'CouchDB',
        6379: 'Redis',
        6667: 'IRC',
        6881: 'BitTorrent',
        8000: 'HTTP alternate',
        8080: 'HTTP alternate',
        8443: 'HTTPS alternate',
        8888: 'HTTP alternate',
        9000: 'SonarQube',
        9090: 'Openfire Administration Console',
        9200: 'Elasticsearch',
        9300: 'Elasticsearch',
        9418: 'Git',
        27017: 'MongoDB',
        27018: 'MongoDB',
        27019: 'MongoDB',
        50000: 'SAP',
        50070: 'Hadoop NameNode',
        50075: 'Hadoop DataNode',
        50090: 'Hadoop Secondary NameNode',
        5601: 'Kibana',
        7077: 'Apache Spark'
    }


def Scan():
    def FullScan(port):
        global OpenPortsList  # tell Python we're using the global list
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((host, port))
            OpenPortsList.append(port)

        except:
            pass
        finally:
            s.close()

    for port in range(0, 500):
        thread = t.Thread(target=FullScan, args=(port,))
        thread.start()

    FullScan(port)

    def Outputs():

        def PortsCheck():
            for port in OpenPortsList:
                if port in CommonPortsList:
                    CommonPortOutput = (f"port {port} is open this port is used for", CommonPortsList.get(port))
                    CommonPortOutputList.append(CommonPortOutput)
                else:
                    UnknownPortOutput = (f"Port {port} is open its use can not be identified by this program")
                    UnknownPortOutputList.append(UnknownPortOutput)

        def ConsoleOutput():
            global CommonPortOutputFiltered
            global CommonPortOutputFilteredDone

            for i in (CommonPortOutputList):
                CommonPortOutputFiltered = f"{i}"

                CommonPortOutputFilteredDone = (
                    CommonPortOutputFiltered.replace("[", "").replace("]", "").replace("'", "").replace(",","").replace("(","").replace(")", ""))

                print(CommonPortOutputFilteredDone + "\n")

            for i in (UnknownPortOutputList):
                UnknownPortOutputFiltered = f"{i}"

                UnknownPortOutputFilteredDone = (
                    UnknownPortOutputFiltered.replace("[", "").replace("]", "").replace("'", "").replace(",","").replace("(", "").replace(")", ""))

                print(UnknownPortOutputFilteredDone + "\n")

        PortsCheck()
        ConsoleOutput()

        def TxtOutput():
            with open('Ports.txt', 'w') as file:
                for CommonPortOutput in CommonPortOutputList:
                    FilteredOutput = str(CommonPortOutput).replace("[", "").replace("]", "").replace("'", "").replace(",", "").replace("(", "").replace(")", "")

                    file.write(FilteredOutput + '\n' + '\n')

                for UnknownPortOutput in UnknownPortOutputList:
                    FilteredOutputU = str(UnknownPortOutput).replace("[", "").replace("]", "").replace("'", "").replace(",", "").replace("(", "").replace(")", "")
                    file.write(FilteredOutputU + '\n' + '\n')

        TxtOutput()

    Outputs()


t1 = t.Thread(target=Scan)
t1.start()