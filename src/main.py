import discord
import openai
import os
from dotenv import load_dotenv

def main():
    
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        async with message.channel.typing():
            completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message.content}
            ]
            )
            await message.channel.send(completion.choices[0].message.content)


    client.run(discord_token)


if __name__ == "__main__":
    try:
        load_dotenv()
    except:
        load_dotenv("../.env")
    openai.api_key = os.getenv("OPENAI_TOKEN")
    discord_token = os.getenv("DISCORD_TOKEN")
    main()