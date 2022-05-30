from datetime import datetime
from netifaces import interfaces, ifaddresses, AF_INET
import netifaces
import requests
import platform
import multiprocessing

def print_datetime():
    print(datetime.utcnow())

def print_interfaces():
    print(netifaces.interfaces())


def print_fisrt_ip():
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])]
    for address in addresses:
        if address != "127.0.0.1" and address != "No IP addr":
            print(address)
            break

def print_external_ip():
    response = requests.get('https://ident.me',timeout=10)
    print(response.content.decode("utf-8"))

def print_CPU_model():
    print(platform.processor())

def print_core_number():
    print(multiprocessing.cpu_count())

if __name__ == '__main__':
    print_datetime()
    print_interfaces()
    print_fisrt_ip()
    print_external_ip()
    print_CPU_model()
    print_core_number()
