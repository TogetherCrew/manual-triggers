from uuid import uuid4
from mongodb_connection import client
from bson.binary import UuidRepresentation
from datetime import datetime

def create_saga(guild_id):
    sagaId = str(uuid4())
    ts = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f+00:00')
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
        },
        "sagaId": sagaId,
        "createdAt": ts,
        "updatedAt": ts
    }
    db = client.get_database("Saga")
    collection = db.get_collection("sagas")
    collection.insert_one(saga)
    return sagaId
