import discord
from openai import OpenAI

DISCORD_TOKEN = "TON_TOKEN_DISCORD"
OPENAI_API_KEY = "TA_CLE_OPENAI"

client_ai = OpenAI(api_key=OPENAI_API_KEY)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot connecté")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = client_ai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Tu es un bot scolaire simple."},
            {"role": "user", "content": message.content}
        ]
    )

    await message.channel.send(response.choices[0].message.content)

client.run(DISCORD_TOKEN)