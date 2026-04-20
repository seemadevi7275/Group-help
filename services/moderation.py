
async def auto_action(count):
    if count == 2:
        return "mute"
    elif count >= 3:
        return "ban"
    return "warn"
