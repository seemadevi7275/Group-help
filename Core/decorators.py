from functools import wraps
from core.permissions import is_admin
from db import get_role

def admin_only(func):
    @wraps(func)
    async def wrapper(update, context):
        if await is_admin(update, context):
            return await func(update, context)
    return wrapper

def mod_only(func):
    @wraps(func)
    async def wrapper(update, context):
        role = await get_role(update.effective_user.id)
        if role in ["mod", "admin"]:
            return await func(update, context)
    return wrapper
