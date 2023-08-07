import portscanner
import ip_info
from printy import printy
import pyfiglet
import subprocess
import sys


# Installing Libraries
def install(package): 
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    # List all required libraries here
required_libraries = ["pyfiglet", "printy", "ping3", "python-nmap"]

    # Check if each library is installed, and install it if not
for library in required_libraries:
    try:
        __import__(library)
        #print(f"{library} is already installed")            
    except ImportError:
        #print(f"{library} is not installed. Installing...")
        install(library)
print('-'*70)


printy(pyfiglet.figlet_format("BK Sec Tool", font="crawford"), "y")

def BK_tool():
    while True:
        print('-'*70)
        print(' ')
        printy("Choose an option:", "y")
        printy('-'*70)
        printy("1. Port Scanner", "y")
        printy("2. IP Information", "y")
        printy("0. Exit", "y")
        choice = input("Enter your choice: ")

        # Call the corresponding script based on the user's choice
        if choice == "1":
            portscanner.main()
        if choice == "2":
            ip_info.IpInfo.get_info()
        elif choice == "0":
            print(" ")
            print("Terminated!")
            print(" ")
            break
            
        
BK_tool()
