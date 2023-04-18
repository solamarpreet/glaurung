import discord
import openai_integration
import config

def run():
    
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
            completion = openai_integration.get_chat_completion(message.content)
            await message.channel.send(completion.choices[0].message.content)


    client.run(config.get_discord_token())