import socket

def get_ip_adress(url):
    result= socket.gethostbyname(url)
    return result