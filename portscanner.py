import socket
import time, datetime
import concurrent.futures
import pyfiglet
from printy import printy
import ping3
import nmap

class Portscanner:

    """
    This class is including some functions like
    Creating banner when the script runs
    Getting user input for target IP and amount of port numbers
    Starting time
    Getting OS info for the target
    Getting FQDN or Host name of the target IP
    Pinging the IP to check if its alive
    Scanning the target for open ports
    End time
    
    """

    @classmethod
    def banner_creation(cls):
            printy(pyfiglet.figlet_format("Port Scanner", font="avatar"), "y")
            print('-'*70)

    @classmethod
    def user_input(cls):
        cls.target = input("Enter target IP: ")
        cls.number_of_ports = int(input("Enter number of ports: "))
        return cls.target, cls.number_of_ports

    @classmethod
    def start_time(cls):
        cls.start = time.time()
        return cls.start

    @classmethod
    def get_os_info(cls, host):
        nm = nmap.PortScanner()
        nm.scan(hosts=host, arguments='-O')
        if host in nm.all_hosts():
            os_info = nm[host]['osmatch'][0]['osclass'][0]
            os_family = os_info['osfamily']
            os_gen = os_info['osgen']
            print(f"[+] Operating system: {os_family} {os_gen}. That might not be acurate. ")
        else:
            print(f"Failed to get Operating System information for {host}")

    @classmethod
    def get_fqdn(cls, target): 
        cls.fqdn = socket.getfqdn(target)
        if cls.fqdn == target:
            print(f"Target {target} has no FQDN or host name.")
        else:
            print(f"[+] FQDN OR Host Name > {cls.fqdn}")

    @classmethod
    def scanner(cls, target, number_of_ports):
        print("[+] The services shown for the ports are general services for these ports.")
        print("    For the real services on the ports, further reconnaissance required.")
        print('')
        printy('Open Ports', "nB")
        print('- '* 7)
        range_of_ports = list(range(1, number_of_ports))
        def binding(*range_of_ports):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Binding target IP to every port number to check if its open.
            for port in range_of_ports:
                s.settimeout(0.1)
                result = s.connect_ex((target, port))
                try:
                    if result == 0:
                        print(port, socket.getservbyport(port))
                except socket.error:
                    print(port)
                    continue 
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(binding, range_of_ports)

    @classmethod
    def pinging(cls):
        cls.response_time = ping3.ping(cls.target, timeout=2)
        print('-'*70)
        if cls.response_time is not None:
            #printy(f"Target is alive. ", "b>")
            Portscanner.get_fqdn(cls.target)
            Portscanner.get_os_info(cls.target)
            Portscanner.scanner(cls.target, cls.number_of_ports)
        else:
            printy(f"Node is down or not responding.", "b>")

    @classmethod
    def end_time(cls):    
        cls.end = time.time()
        cls.time_took = str(cls.end-cls.start)
        x = slice(0, 4)
        print('-'*70)
        print(f'\nTime took in second: {cls.time_took[x]}')
        print('<', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '>\n')


def main():
    Portscanner.banner_creation()
    Portscanner.user_input()
    Portscanner.start_time()
    Portscanner.pinging()
    Portscanner.end_time()



if __name__ == "__main__":
    main()
