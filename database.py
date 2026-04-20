
roles = db["roles"]

async def set_role(user_id, role):
    await roles.update_one(
        {"user_id": user_id},
        {"$set": {"role": role}},
        upsert=True
    )

async def get_role(user_id):
    data = await roles.find_one({"user_id": user_id})
    return data["role"] if data else "user"
