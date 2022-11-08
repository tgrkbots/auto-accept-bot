from pyrogram.errors import UserChannelsTooMuch, UserNotParticipant
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import os,time


CHATID = int(os.environ.get('CHAT_ID', -1001332181134))


BOT_TOKEN = os.environ.get(
    'BOT_TOKEN', '5423826084:AAG5ESfMQPvDRgVv8dwcWWzgkt6sgVh1Wno')

API_ID = 16514976
API_HASH = '40bd8634b3836468bb2fb7eafe39d81a'
app = Client("ApprovalReqBot", api_id=API_ID,
             api_hash=API_HASH, bot_token=BOT_TOKEN)

about_txt = '''**🤖 Name :**  Auto Accepter Bot
**🔠 Language  :** Python3.10.8
**📚 Library   :** Pyrogram
**🧑🏻‍💻 Developer :** @YourInviteLink
©️ Powered By @CrazeBots'''

start_btns = InlineKeyboardMarkup([
    [InlineKeyboardButton("Help 🆘", callback_data="help_data"),
     InlineKeyboardButton("About ME 🤖", callback_data="about_data"),
     ],
    [InlineKeyboardButton("Updates Channel 📣", url="https://t.me/crazebots"
                          ), ]
])


@app.on_message(filters.command('start'))
def start_cmd(_, M):
    try:
        app.get_chat_member(CHATID,M.chat.id)
    except UserNotParticipant:
        app.send_message(M.chat.id, 'Please Join My **Updates Channel** to Use Me!!', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Updates Channel 📣",url="https://t.me/crazebots"),]]))
        return

    text = f"Hello {M.from_user.mention} 👋\n\n<b>I'm an auto approve Admin Join Requests Bot.\n\n<b>I can approve users in Groups/Channels.</b>Add me to your chat and promote me to admin with add members permission.</b>"
    app.send_photo(
        M.chat.id, 'https://telegra.ph/file/83dd5336328b882bcfea0.jpg', text, reply_markup=start_btns)


about_btns = InlineKeyboardMarkup([
    [InlineKeyboardButton("◀️ Back️ To Home 🏠", callback_data="back_data"), ],
])

button = InlineKeyboardMarkup([
    [InlineKeyboardButton("Join Updates Channel 📣", url="https://t.me/crazebots"), ],
])


@app.on_callback_query(filters.regex('help_data'))
def helpfun(_, msg: CallbackQuery):
    msg.edit_message_caption(
        '''<b>Usage instructions.</b>

Add me to your channel, as administrator, with "add users" permission, and i will start accepting new members request!

To approve members who are already in waiting.''', reply_markup=about_btns)


@app.on_callback_query(filters.regex('about_data'))
def helpfun(_, msg: CallbackQuery):
    msg.edit_message_caption(about_txt, reply_markup=about_btns)


@app.on_callback_query(filters.regex('back_data'))
def back_handler(_, msg: CallbackQuery):
    msg.edit_message_caption(
        f"Hello {msg.from_user.mention} 👋\n\n<b>I'm an auto approve Admin Join Requests Bot.\n\n<b>I can approve users in Groups/Channels.</b>Add me to your chat and promote me to admin with add members permission.</b>", reply_markup=start_btns)


@app.on_chat_join_request()
def reqs_handler(client: app, message: ChatJoinRequest):
    chatid = message.chat

    user = message.from_user
    time.sleep(5)

    try:
        app.approve_chat_join_request(chatid.id, user.id)
        app.send_message(
            user.id, f'<b>Hello</b> {user.mention}\n\nYour Request To Join <b>{chatid.title}</b> has been approved!', reply_markup=button)

    except UserChannelsTooMuch:
        pass

    except Exception as ex:
        print(ex)


print('Bot Started')
app.run()
