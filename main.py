from mongodb_connection import client
from helpers.get_guilds import get_guilds
from helpers.print_guilds import print_guilds
from helpers.workflow import workflow


def ask_for_confirmation(guilds):
    if len(guilds) == 1:
        guild = guilds[0]
        confirmation = input(
            f"Are you sure you want to continue with {guild['name']} (y/n): ")
        return confirmation.lower() == 'y'
    elif len(guilds) > 1:
        print("You've entered multiple guilds. Please confirm each one:")
        for guild in guilds:
            print(f"${guild['guildId']} - ${guild['name']}")
        confirmation = input(
            "Are you sure you want to continue with all these guilds (y/n): ")
        return confirmation.lower() == 'y'
    else:
        confirmation = input(
            "Are you sure you want to continue with ALL guilds? (y/n): ")
        return confirmation.lower() == 'y'

def main():

    print("Welcome to Manual Triggers!")

    db = client.get_default_database()
    guilds = get_guilds(db=db)

    print_guilds(guilds)

    guild_ids = input(
        "Enter guildIds separated by commas (or leave blank to continue on all guilds): ")
    guild_ids = [guild_id.strip()
                 for guild_id in guild_ids.split(",")] if guild_ids else []

    if not guild_ids:
        if not ask_for_confirmation(guild_ids):
            print("Exiting script.")
            return
    else:
        guilds = list(db["guilds"].find(
            {"guildId": {"$in": guild_ids}}, {"name": 1, "guildId": 1}))
        if not guilds:
            print("No matching guilds found. Exiting script.")
            return

        if not ask_for_confirmation(guilds):
            print("Exiting script.")
            return

    workflow(guild_ids)

if __name__ == "__main__":
    main()
