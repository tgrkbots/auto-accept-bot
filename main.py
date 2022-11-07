from pyrogram.errors import UserChannelsTooMuch,FloodWait
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
import os

ch1_link=os.environ.get('CH1_LINK','https://t.me/crazebots')
ch2_link=os.environ.get('CH2_LINK','https://t.me/crazebots')


ch1_title=os.environ.get('CH1_TITLE','👉 Channel 1 👈')
ch2_title=os.environ.get('CH2_TITLE','👉 Channel 2 👈')


BOT_TOKEN=os.environ.get('BOT_TOKEN','5423826084:AAG5ESfMQPvDRgVv8dwcWWzgkt6sgVh1Wno')

API_ID = 16514976
API_HASH = '40bd8634b3836468bb2fb7eafe39d81a'
app = Client("ApprovalReqBot", api_id=API_ID,
             api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command('start'))
def start_cmd(_, M):
    #button2 = [[ InlineKeyboardButton("🆎 About", callback_data="aboutbtn"), InlineKeyboardButton("🆘 Help", callback_data="helpbtn") ],]
    text = f"Hello {M.from_user.mention} 👋\n\nI'm an auto approve Admin Join Requests Bot.\n\n<b>I can approve users in Groups/Channels.</b>Add me to your chat and promote me to admin with add members permission."
    app.send_photo(
        M.chat.id, 'AgACAgEAAxkBAAIBQWNoe2BujKjijWmZI4a-G-zZmvbMAAIhqjEbQk1JR4ajQGkMIqBJAAgBAAMCAAN5AAceBA', text)


button = [[InlineKeyboardButton(f"{ch1_title}", url=f"{ch1_link}")],[InlineKeyboardButton(f"{ch2_title}", url=f"{ch2_link}")],]

@app.on_chat_join_request()
def reqs_handler(client: app, message: ChatJoinRequest):
    chatid = message.chat

    user = message.from_user

    try:
        app.approve_chat_join_request(chatid.id, user.id)
        app.send_message(user.id, f'<b>Hello</b> {user.mention}\n\nYour Request To Join <b>{chatid.title}</b> has been approved!',reply_markup=InlineKeyboardMarkup(button))

    except UserChannelsTooMuch:
        pass

    except Exception:
        print(Exception)


print('Bot Started')
app.run()
