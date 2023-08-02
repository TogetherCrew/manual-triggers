import uuid
from mongodb_connection import client
from bson.objectid import ObjectId

def create_saga(guild_id):
    saga = {
        "choreography": {
            "name": "MANUAL_ANALYZER",
            "transactions": [
                {
                    "queue": "DISCORD_ANALYZER",
                    "event": "RUN",
                    "order": 1,
                    "status": "NOT_STARTED",
                    "start": {
                        "$date": "2023-07-28T14:05:43.230Z"
                    },
                    "end": {
                        "$date": None
                    },
                    "runtime": None
                }
            ]
        },
        "status": "NOT_STARTED",
        "data": {
            "guildId": guild_id
        }
    }
    db = client.get_database("Saga")
    collection = db.get_collection("sagas")
    result = collection.insert_one(saga)
    object_id = ObjectId(result.inserted_id)
    document = collection.find_one({ "_id": object_id })
    print(document)
    return document.sagaId
