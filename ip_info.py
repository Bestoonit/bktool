import requests
import json

class IpInfo:
    @classmethod
    def get_info(cls):
        ip=input("Enter IP address: ")
        format = "json"
        url=(f'https://ipapi.co/{ip}/{format}/')

        response = requests.get(url)
        response_in_json = response.json()
        indented_json = json.dumps(response_in_json, indent=2)
        print('-'*70)
        if "error" in indented_json:
            print(f"{response_in_json['reason']}. Try a public IP Address!")
        elif "error" not in indented_json:
            print(indented_json)

def main():
    IpInfo.get_info()

if __name__ == "__main__":
    main()    
