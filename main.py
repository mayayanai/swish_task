from flask import Flask, jsonify
from datetime import datetime
from netifaces import interfaces, ifaddresses, AF_INET
import netifaces
import requests
import platform
import multiprocessing
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import GPUtil
import psutil
from hurry.filesize import size


app = Flask(__name__)

@app.route('/')
def return_info():
    return prepare_response()


def get_datetime():
    return datetime.utcnow()

def get_interfaces():
    return netifaces.interfaces()


def get_first_ip():
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])]
        for address in addresses:
            if address != "127.0.0.1" and address != "No IP addr":
                return (address)


def get_external_ip():
    response = requests.get('https://ident.me',timeout=10)
    return response.content.decode("utf-8")

def get_CPU_model():
    return platform.processor()

def get_core_number():
    return multiprocessing.cpu_count()

def get_GPU_type():
    GPU_count =0
    GPU_list = GPUtil.getAvailable()
    for x in GPU_list:
        GPU_count += 1
    if GPU_count == 0:
        return "No GPU found"
    return GPU_list

def get_memory_size():
    return size(psutil.virtual_memory()[0])

def prepare_response():
    return jsonify(
        date_and_time=get_datetime(),
        interfaces=get_interfaces(),
        first_ip=get_first_ip(),
        external_ip=get_external_ip(),
        cpu_model=get_CPU_model(),
        core_number=get_core_number(),
        GPU_type=get_GPU_type(),
        memory_size=get_memory_size()
    )


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)