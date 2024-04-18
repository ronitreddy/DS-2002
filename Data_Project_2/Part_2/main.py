# Import necessary libraries and modules
from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# Load Discord bot token from environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configure bot intents to handle messages
intents: Intents = Intents.default()
intents.message_content = True  # Enable reading message content
client: Client = Client(intents=intents)

# Initialize a dictionary to maintain shopping cart for each user
user_carts = {}

# Define a function to process and send messages
async def send_message(message: Message,user_message: str) -> None:
    # Early exit if the user message is empty
    if not user_message:
        print('(Message was empty because intents were not enabled...prob)')
        return
    # Check if a cart exists for the user, if not, create an empty one
    if message.author.id not in user_carts:
        user_carts[message.author.id] = {}
    # Determine if the message should be sent privately
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]  # Remove the private command indicator
    try:
        # Retrieve the user's cart
        user_cart = user_carts[message.author.id]
        # Generate response based on the user message, user cart, and user ID
        response = get_response(message.author.id, user_message, user_cart)
        # Send response privately or to the channel based on is_private flag
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        # Log any errors encountered during message sending
        print(e)

# Event handler for when the bot is ready and operational
@client.event
async def on_ready() -> None:
    # Notify that the bot is operational
    print(f'{client.user} is now running!')

# Event handler for incoming messages
@client.event
async def on_message(message: Message) -> None:
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return
    # Log incoming messages for debugging
    username: str= str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    print(f'[{channel}] {username}: "{user_message}"')
    # Process and send a response to the message
    await send_message(message, user_message)

# Define the main function to start the bot
def main() -> None:
    # Run the bot with the specified token
    client.run(token=TOKEN)

# Ensure the script runs the main function when executed directly
if __name__ == '__main__':
    main()