import requests
import discord

client = discord.Client()

bot_token = "MTAwNjQzODE3MzYwMzI2NjYyMA.GA6BqK.K9-E1cLwVMAzYdPyYrzOCzlvXpIxfDv9k4Cg84"
api_url = "https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD"

response = requests.get(api_url)

data = response.json()

for j in data:
    currency = j['name']
    time = j['time']
    price = j['basePrice']
    opening = j['openingPrice']

changes = (price - opening) / opening * 100

@client.event
async def on_ready():
    print("Logged in as ")
    print(client.user.name)
    print(client.user.id)
    print("===========")

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Currency Charts"))


@client.event
async def on_message(message):
    if message.author.bot:
        return None
    channel = message.channel

    if message.content.startswith('!달러환율'):
        await message.channel.send(f"기준 시간: {time}\n{currency}\n현재가: {price}원\n전일가: {opening}원\n변동률: {round(changes, 2)}%")


client.run(bot_token)
