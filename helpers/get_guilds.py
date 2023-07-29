from mongodb_connection import client

def get_guilds(db=client.get_default_database()):
    collection = db["guilds"]
    guilds = collection.find({}, {"name": 1, "guildId": 1})
    return guilds