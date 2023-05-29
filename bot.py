from pyrogram import Client, filters

# Put your API ID, API hash, and bot token here

api_id = "2912653"

api_hash = "36a616c83fb35db05d768b40cd18242b"

bot_token = "6232405745:AAH9ZyV6ovSP1BuOSJDzg1BXHbnu9GublI0"

# Create a new Pyrogram client

app = Client("juju1", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))

def start_command(client, message):

    # Send a welcome message

    client.send_message(message.chat.id, "Bot is now started!")

# Start the client

app.run()
