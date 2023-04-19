import discord
import openai_integration
import config


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    async with msg.channel.typing():
        completion = openai_integration.completion_handler(msg)
        await msg.channel.send(completion)


client.run(config.get_discord_token())