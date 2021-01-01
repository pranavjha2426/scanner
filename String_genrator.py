from telethon.sync import TelegramClient

from telethon.sessions import StringSession

print(

    """Please go-to my.telegram.org

Login using your Telegram account

Click on API Development Tools

Create a new application, by entering the required details"""

)

APP_ID = int(input("2327886: "))

API_HASH = input("b27fc6b63c22a6917438a57bc616075c: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:

    print(client.session.save())
