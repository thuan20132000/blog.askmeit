import requests
from bs4 import BeautifulSoup

# from random import choice
import random


def save_proxies(ip_list, port_list, number):
    # proxy_list = list()

    proxy_data = open('dictionary/proxy_data.txt', 'w')
    for x in range(number):
        proxy = f"{ip_list[x]}:{port_list[x]}"
        # proxy_list.append(proxy)
        proxy_data.write(proxy+"\n")


def generate_proxy():

    response = requests.get("https://sslproxies.org/")
    soup = BeautifulSoup(response.content, 'html5lib')
    ip_list = list()
    port_list = list()

    td_ip_list = soup.findAll('td')[::8]
    td_port_list = soup.findAll('td')[1::8]
    for ip in td_ip_list:
        ip_list.append(ip.text)
    for port in td_port_list:
        port_list.append(port.text)

    save_proxies(ip_list, port_list, 20)


def choose_random(file_name):
    """Choose a line at random from the text file"""
    with open(file_name, 'r') as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        print(random_line)

    return random_line


def downloadFileFromUrl(proxy, file_url, file_name):
    # sound_uk = 'https://www.oxfordlearnersdictionaries.com/media/english/uk_pron/a/abs/absol/absolute__gb_1.mp3'
    count = 1

    while True:
        try:
            print(f"downloading {file_name} turn {count} with proxy: {proxy}")
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

            if count > 6:
                # generate_proxy()
                # print('Generate new proxy')
                # count = 1
                proxy = choose_random("dictionary/proxy_data.txt")
                count += 1
                if count > 10:
                    generate_proxy()
                    count = 1
                    continue

            proxy_data = {
                "http": f"http://{proxy}",
                "https": f"https://{proxy}"
            }

            response = requests.get(
                file_url, headers=headers, timeout=17, proxies=proxy_data)

            f = open(f'dictionary/audio/{file_name}', 'wb')
            f.write(response.content)
            return

        except Exception as e:
            print("Error at download file ", file_name)
            print("error message: ", e)
            count += 1
            continue
