import requests
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

bot_token = "MTAwNjQzODE3MzYwMzI2NjYyMA.GJM6XM.8pFw_1GcoQriZrfhFMEGYyl9UvmZoCr8VujGIU"


@client.event
async def on_ready():
    print("Logged in as ")
    print(client.user.name)
    print(client.user.id)
    print("===========")

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Currency Charts"))


@client.command(name='달러환율') #달러 환율 리퀘스트 일시 Trigger
async def on_message(message):
    api_url = "https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD"
    response = requests.get(api_url)

    data = response.json()

    for j in data:
        currency = j['name']
        time = j['time']
        price = j['basePrice']
        opening = j['openingPrice']

    changes = (price - opening) / opening * 100
    await message.send(f"기준 시간: {time}\n{currency}\n현재가: {price}원\n전일가: {opening}원\n변동률: {round(changes, 2)}%") 

@client.command(name='원달러')
async def KRWUSD(ctx, dollars):
    api_url = "https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD"
    response = requests.get(api_url)

    data = response.json()

    for j in data:
        price = j['basePrice']
    
    krw = int(price) * int(dollars)
    await ctx.send(f"${dollar}은 현재 환율로 {krw}원 입니다.")



client.run(bot_token)
