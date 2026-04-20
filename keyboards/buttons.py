
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_panel():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⚙️ Settings", callback_data="settings")],
        [InlineKeyboardButton("📊 Stats", callback_data="stats")]
    ])
