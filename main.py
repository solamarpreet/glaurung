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

        response = openai.Completion.create(model="text-davinci-003", max_tokens=2048, prompt=message.content)
        await message.channel.send(response.choices[0].text.strip())

    client.run(discord_token)


if __name__ == "__main__":
    load_dotenv("")
    openai.api_key = os.getenv("OPENAI_TOKEN")
    discord_token = os.getenv("DISCORD_TOKEN")
    main()