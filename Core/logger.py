
from config import LOG_CHAT_ID

async def log(context, text):
    if LOG_CHAT_ID:
        await context.bot.send_message(LOG_CHAT_ID, text)
