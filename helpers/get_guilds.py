def get_guilds(db):
    collection = db["guilds"]
    guilds = collection.find({}, {"name": 1, "guildId": 1})
    return guilds