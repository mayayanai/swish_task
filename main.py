from datetime import datetime
from netifaces import interfaces, ifaddresses, AF_INET
import netifaces
import requests
import platform
import multiprocessing
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.python.client import device_lib
import psutil
from hurry.filesize import size

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

def print_GPU_type():
    local_device_protos = device_lib.list_local_devices()
    GPU_count =0
    for x in local_device_protos:
        if x.device_type == 'GPU':
            GPU_count += 1
            print (x.name)
    if GPU_count == 0:
        print("No GPU found")

def print_memory_size():
    print(size(psutil.virtual_memory()[0]))

if __name__ == '__main__':
    print_datetime()
    print_interfaces()
    print_fisrt_ip()
    print_external_ip()
    print_CPU_model()
    print_core_number()
    print_GPU_type()
    print_memory_size()