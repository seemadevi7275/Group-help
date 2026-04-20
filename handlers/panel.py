
from telegram import Update
from telegram.ext import ContextTypes
from keyboards.buttons import main_panel

async def panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎛 Control Panel",
        reply_markup=main_panel()
    )
