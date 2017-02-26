import os

def get_whois(url):
    command = "whois"+" "+url
    process = os.popen(command)
    results = str(process.read())
    return results

print("Whois starting")
# print(get_whois("gerardo.lt"))