
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters
)

from config import TOKEN
from handlers.admin import warn
from handlers.user import message_handler
from handlers.system import welcome
from handlers.panel import panel

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("warn", warn))
app.add_handler(CommandHandler("panel", panel))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
app.add_handler(CallbackQueryHandler(panel))

app.run_polling()
