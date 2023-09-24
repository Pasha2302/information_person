import requests
import json

# URL-адрес веб-хука Discord
webhook_url = "https://discord.com/api/webhooks/1155208823024398397/8gW4zbXp-sA4hIivOTca0WNajcOgG21e7UyXHhAeVXwFn8dGFY0Xf5XWozz_2Gxn_Qhm"

# Текст сообщения, которое вы хотите отправить
message = "Привет, это сообщение отправлено с помощью веб-хука Discord и Python!"

# Создайте словарь с данными для сообщения
data = {
    "content": message
}

# Преобразуйте словарь в JSON-формат
json_data = json.dumps(data)

# Отправьте POST-запрос на веб-хук Discord
response = requests.post(webhook_url, data=json_data, headers={"Content-Type": "application/json"})

# Проверьте статус ответа
if response.status_code == 204:
    print("Сообщение успешно отправлено на веб-хук Discord!")
else:
    print(f"Произошла ошибка при отправке сообщения. Код состояния: {response.status_code}")
