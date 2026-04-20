
import time

cooldowns = {}

def check_cooldown(user_id, command, limit=5):
    key = f"{user_id}:{command}"
    now = time.time()

    if key in cooldowns and now - cooldowns[key] < limit:
        return False

    cooldowns[key] = now
    return True
