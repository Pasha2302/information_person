<p align="center">
    <a href="https://#">
      <img src="https://img.shields.io/badge/-TWITTER-black?logo=twitter&style=for-the-badge">
    </a>
    &nbsp;
    <a href="https://#">
      <img src="https://img.shields.io/badge/-spyboy.in-black?logo=google&style=for-the-badge">
    </a>
    &nbsp;
    <a href="https://#">
      <img src="https://img.shields.io/badge/-spyboy.blog-black?logo=wordpress&style=for-the-badge">
    </a>
    &nbsp;
    <a href="https://#">
      <img src="#">
    </a>
  
</p>

<img width="100%" align="centre" src="#" />

<h3 align="center"> Отслеживайте IP-адрес и местоположение по GPS смартфона или ПК пользователя и делайте снимки цели вместе с информацией об устройстве. </h3>

Инструмент размещает поддельный веб-сайт, который использует iframe для отображения настоящего веб-сайта, и, если цель позволяет это, он получит местоположение GPS «(широта и долгота)» цели, захватит несколько изображений цели вместе с «IP». Адрес» и «Информация об устройстве».

<h4 align="center"> Этот инструмент является проверкой концепции и предназначен только для образовательных целей. </h4> 

Используя этот инструмент, вы можете узнать, какую информацию вредоносный веб-сайт может собрать о вас и ваших устройствах и почему вам не следует нажимать на случайные ссылки или предоставлять им такие разрешения, как местоположение.

### Ключевая особенность:

- IP-адрес и отслеживание географического местоположения
- Сбор информации о системе устройства
- Захват изображений с камеры устройства
- Интеграция с Discord для представления данных
- Взаимодействие с пользователем для разрешения местоположения
- Отображение сайта через встроенный iframe
- Регулярный сбор данных на основе интервалов
- Доступ к изображениям с веб-камеры и их загрузка.
- Форматирование и представление данных в сообщениях Discord
- Ссылки на Google Maps и Google Earth в зависимости от местоположения.
- Обработка ошибок при отказе в разрешении на определение местоположения.
- Отзывы пользователей и сообщения об ошибках
---
### On the link click

```diff
+ Он автоматически получит IP-адрес и информацию об устройстве
! Если разрешение на определение местоположения разрешено, оно получит точное местоположение цели.
! Если разрешено разрешение камеры, она будет непрерывно снимать с передней камеры.
```

### Limitation

```diff

- Обязательно перенесите порт вперед, иначе он не будет работать в браузере смартфона.
# Большинство браузеров автоматически блокируют дополнительные разрешения для URL-адресов на основе IP. так порт вперед!!
- Он не будет работать на ноутбуках или телефонах без GPS или камеры.
# браузеры, блокирующие JavaScript,
# или если цель имитирует местоположение GPS.
# или если цель использует VPN или подменяет IP-адрес

- Некоторые браузеры автоматически блокируют разрешение на определение местоположения, например (Brave, Safari и т. д.)

+ Лучшая работа с браузером Chrome
+ Точность определения местоположения будет более точной, если вы используете это на смартфоне.

```

### IP location VS. GPS location

```diff
- Географическое местоположение на основе IP-адреса НЕ является точным,
# Не указывает местоположение цели.
# Вместо этого он предоставляет приблизительное местоположение интернет-провайдера (провайдера Интернет-услуг)
```
```разница
+ GPS определяет почти точное местоположение, поскольку использует координаты долготы и широты.
@@ После получения разрешения на определение местоположения @@
# Точная информация о местоположении поступает на расстоянии от 20 до 30 метров от местоположения пользователя.
# (это почти точное место)
```
---

<h4 align="center">
  OS compatibility :
  <br><br>
  <img src="https://img.shields.io/badge/Windows-05122A?style=for-the-badge&logo=windows">
  <img src="https://img.shields.io/badge/Linux-05122A?style=for-the-badge&logo=linux">
  <img src="https://img.shields.io/badge/Android-05122A?style=for-the-badge&logo=android">
  <img src="https://img.shields.io/badge/macOS-05122A?style=for-the-badge&logo=macos">
</h4>

<h4 align="center"> 
Requirements:
<br><br>
<img src="https://img.shields.io/badge/Python-05122A?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Git-05122A?style=for-the-badge&logo=git">
<img src="https://img.shields.io/badge/Discord webhook-05122A?style=for-the-badge&logo=discord">
</h4>

### ⭔ Installation
---

```
git clone https://github.com/Pasha2302/information_person.git
```
```
cd information_person
```
```
pip3 install -r requirements.txt
```

`NOTE:` If you're not going to use `localhost` `(http://127.0.0.1:8000)`

Пожалуйста, `измените` [this](https://github.com/spyboy-productions/r4ven/blob/6e5230d309a4a3acf0d7a67a8e3913ccc35f7124/index.html#L203C29-L203C50) строку с URL-адресом, который вы хотите использовать.

```
python3 main.py
```

```Введите URL-адрес веб-перехватчика Discord (настройте канал на сервере Discord с интеграцией веб-перехватчика).)```

https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks

`Если у вас нет учетной записи Discord и вы можете создать ее, это бесплатно.`

https://discord.com/

---

📍 _Данные трека будут отправлены на ваш канал веб-перехватчика Discord._

- Почему дискорд вебхук? Удобно, что вы получите уведомление, когда кто-то нажмет на ссылку.

---

#### ⭓ Чтобы изменить шаблон сайта

- открыть файл `index.html` в строке 12 и замените`src` in the iframe. (Примечание: не все веб-сайты поддерживают iframe)

---

#### ⭓ Чтобы перенаправить порт, установите ngrok или используйте ssh или любой другой инструмент, с помощью которого вы хотите перенаправить порт.

- For ngrok port forward type: ngrok http 8000
- For ssh port forwarding type: ssh -R 80:localhost:8000 ssh.localhost.run

```diff
- Предупреждение: обязательно перенесите порт вперед, иначе он не будет работать в браузере смартфона.
```

---

#### 💬 Если возникла проблема [Обсудите здесь] (https://#)
[![Discord Server](https://discord.com/api/guilds/726495265330298973/embed.png)](https://discord.gg/ZChEmMwE8d)

### ⭔ Снимки
---
<img width="100%" align="centre" src="https://cdn.discordapp.com/attachments/748888788490780721/979508653205913650/Screen_Shot_2022-05-27_at_3.40.19_AM.png" />
<img width="100%" align="centre" src="https://cdn.discordapp.com/attachments/748888788490780721/980448995958722650/Screen_Shot_2022-05-29_at_5.55.48_PM.png" />
<img width="100%" align="centre" src="https://cdn.discordapp.com/attachments/748888788490780721/980449483684982834/Screen_Shot_2022-05-29_at_6.05.44_PM.png" />
