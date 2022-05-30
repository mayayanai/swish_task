from datetime import datetime
from netifaces import interfaces, ifaddresses, AF_INET
import netifaces

def print_datetime():
    print(datetime.utcnow())

def print_interfaces():
    print(netifaces.interfaces())


def print_fisrt_ip():
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])]
    for address in addresses:
        if address != "127.0.0.1":
            print(address)
            break


if __name__ == '__main__':
    print_datetime()
    print_interfaces()
    print_fisrt_ip()
