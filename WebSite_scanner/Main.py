from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from who_is import *

ROOT_DIR = "companies"
create_dir(ROOT_DIR)

def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip_adress = get_ip_adress(domain_name)
    nmap = get_nmap("-F", ip_adress)
    robots_txt= get_robots_txt(url)
    whois= get_whois(domain_name)

    create_report( name, url, domain_name, nmap, robots_txt, whois)


def create_report(name, url, domain_name, nmap, robots_txt, whois):
    project_dir= ROOT_DIR + "/" + name
    create_dir(project_dir)
    write_file(project_dir + "/full_url.txt", url)
    print("Creating full_url.txt")
    write_file(project_dir + "/domain_name.txt", domain_name)
    print("Creating domain_name.txt")
    write_file(project_dir + "/nmap.txt", nmap)
    print("Creating nmap.txt")
    write_file(project_dir + "/robots_txt.txt", robots_txt)
    print("Creating robots.txt")
    write_file(project_dir + "/whois.txt", whois)
    print("Creating whois.txt")

gather_info("google", "http://www.google.com")