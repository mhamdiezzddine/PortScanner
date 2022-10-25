import socket
from IPy import IP

#scanning multiple targets
def scan(target):

    converted_ip = check_ip(target)
    print ('\n' + '[-O- Scanning Target ]' + str(target))
    
    for port in range(1,1024):
        scan_port(converted_ip,port)    

# domain name --> ip
def check_ip(ip):
    
    try:
        #convert to ip format
        IP(ip)
        return(ip)

    #return valueError if the ip is domain name
    except ValueError:
        #convert the domain name to ip address
        return socket.gethostbyname(ip)

def get_banner(socket):
    #receive information with 1024 bit
    return socket.receive(1024)


def scan_port (ip, port) :
    try :

        #create socket descriptor
        socket = socket.scoket() 
        #accelerate the scan
        socket.settimeout(0.5)
        #establish a connection with the target 
        socket.connect()
        try :

            #get banner 
            banner = socket.get_banner(socket)
            print ('[+] Open port ' + str(port) + ' : '+str(banner).decode().strip('\n'))
        except:
            print ('[+] Open port ' + str(port))

    except :
        #print ('[-] Port ' + str(port) + ' Is Closed')

        #pass the closed ports 
         pass


if __name__== "__main__":

    #this is for multiple variables
    targets = input ('[+] Enter Targets To Scan : (For multiple target just tseperate them with ',') ')


    if ',' in targets:
        for ip_address in targets.split(','):
            scan(ip_address.strip(' '))
    else:
        scan(targets)






