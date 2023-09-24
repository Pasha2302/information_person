"""
Purpose: will hold the util functions of the program
"""
import json
import requests


def get_file_data(file_path):
    """
    Получает данные файла
     :param file_path: путь к файлу, который вы хотите прочитать.
     :return: Данные файла в виде обычного текста
    """
    with open(file_path, 'r') as open_file:
        return open_file.read()


def update_webhook(webhook: str, webhook_data: dict):
    """
    Отправит запрос на публикацию на указанный вебхук
     :param webhook: Вебхук, который вы хотите обновить
    """
    request_payload = json.dumps(webhook_data)
    headers = {'Content-Type': 'application/json'}
    requests.request("POST", webhook, headers=headers, data=request_payload)
