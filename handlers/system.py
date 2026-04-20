
from services.anti_raid import raid_detected

async def welcome(update, context):
    if raid_detected():
        await update.message.reply_text("🚨 Raid detected! Locking group")
        await context.bot.set_chat_permissions(
            update.effective_chat.id,
            permissions={"can_send_messages": False}
        )
        return

    for user in update.message.new_chat_members:
        await update.message.reply_text(f"👋 Welcome {user.first_name}")
