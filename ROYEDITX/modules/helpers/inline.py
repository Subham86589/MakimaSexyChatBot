from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from ROYEDITX import BOT_USERNAME, OWNER

DEV_OP = [
    [
        InlineKeyboardButton(
            text="𝙃𝙄𝙅𝘼𝘾𝙆 𝙈𝙀⚡",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="𝙎𝙊𝙐𝙍𝘾𝙀⚡", callback_data="SOURCE"),
        InlineKeyboardButton(text="𝙊𝙒𝙉𝙀𝙍⚡⚡", url=f"https://t.me/hewasSUBBU"),
    ],
    [
        InlineKeyboardButton(text="𝙃𝙀𝙇𝙋𝙎 & 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎⚡", callback_data="HELP"),
    ],
]

####
PNG_BTN = [
    [
        InlineKeyboardButton(
            text="𝙃𝙄𝙅𝘼𝘾𝙆 𝙈𝙀⚡",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
        InlineKeyboardButton(text="𝙊𝙒𝙉𝙀𝙍⚡", url=f"https://t.me/hewasSUBBU"),
    ],
]

#####
BACK = [
    [
        InlineKeyboardButton(text="𝘽𝘼𝘾𝙆⚡", callback_data="BACK"),
    ],
]


####
HELP_BTN = [
    [
        InlineKeyboardButton(text="𝘽𝘼𝘾𝙆⚡", callback_data="BACK"),
        InlineKeyboardButton(text="𝘾𝙇𝙊𝙎𝙀⚡", callback_data="CLOSE"),
    ],
]

#####
CLOSE_BTN = [
    [
        InlineKeyboardButton(text="𝙐𝙋𝘿𝘼𝙏𝙀𝙎⚡", url=f"https://t.me/sukunaxsupport"),
        InlineKeyboardButton(text="𝘾𝙇𝙊𝙎𝙀⚡", callback_data="CLOSE"),
    ],
]

####
CHATBOT_ON = [
    [
        InlineKeyboardButton(text="𝙀𝙉𝘼𝘽𝙇𝙀⚡", callback_data=f"addchat"),
        InlineKeyboardButton(text="𝘿𝙄𝙎𝘼𝘽𝙇𝙀⚡", callback_data=f"rmchat"),
    ],
]

#####
CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="𝘽𝘼𝘾𝙆⚡", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="𝘾𝙇𝙊𝙎𝙀⚡", callback_data="CLOSE"),
    ],
]

####
HELP_START = [
    [
        InlineKeyboardButton(text="𝙃𝙀𝙇𝙋⚡", callback_data="HELP"),
        InlineKeyboardButton(text="𝘾𝙇𝙊𝙎𝙀⚡", callback_data="CLOSE"),
    ],
]

#####
HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="𝙃𝙀𝙇𝙋⚡", url=f"https://t.me/{BOT_USERNAME}?start=help"
        ),
        InlineKeyboardButton(text="𝘾𝙇𝙊𝙎𝙀⚡", callback_data="CLOSE"),
    ],
]

######
