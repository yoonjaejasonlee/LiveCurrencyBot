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


@client.command(name='달러환율')  # 달러 환율 리퀘스트 일시 Trigger
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
    embed = discord.Embed(title="달러 얼마니?", description=f"{currency}", color=0xA71313)  # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
    embed.add_field(name="기준 시간", value=f"{time}")
    embed.add_field(name="현재가", value=f"{price}원")
    embed.add_field(name="전일가", value=f"{opening}원")
    embed.add_field(name="변동률", value=f"{round(changes, 2)}%")
    embed.set_footer(text="show me the money by yoonj#0492", icon_url="https://spng.pngfind.com/pngs/s/31-317340_stack-of-money-png-pile-of-money-transparent.png")  # 하단에 들어가는 조그마한 설명을 잡아줍니다
    await message.send(embed=embed)

@client.command(name='유로환율')  # 유로 환율 리퀘스트 일시 Trigger
async def on_message(message):
    api_url = "https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWEUR"
    response = requests.get(api_url)

    data = response.json()

    for j in data:
        currency = j['name']
        time = j['time']
        price = j['basePrice']
        opening = j['openingPrice']

    changes = (price - opening) / opening * 100
    embed = discord.Embed(title="유로 얼마니?", description=f"{currency}", color=0xA71313)  # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
    embed.add_field(name="기준 시간", value=f"{time}")
    embed.add_field(name="현재가", value=f"{price}원")
    embed.add_field(name="전일가", value=f"{opening}원")
    embed.add_field(name="변동률", value=f"{round(changes, 2)}%")
    embed.set_footer(text="show me the money by yoonj#0492", icon_url="https://spng.pngfind.com/pngs/s/31-317340_stack-of-money-png-pile-of-money-transparent.png")  # 하단에 들어가는 조그마한 설명을 잡아줍니다
    await message.send(embed=embed)


@client.command(name='원달러')  # 환전값
async def KRWUSD(ctx, dollars):
    api_url = "https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD"
    response = requests.get(api_url)

    data = response.json()

    for j in data:
        price = j['basePrice']

    krw = int(price) * int(dollars)
    plus_duty = krw + (krw * 0.23)
    embed = discord.Embed(title=f"${dollars}은 현재 환율로 {krw}원 입니다.", color=0xA71313)
    embed.add_field(name="예상 관부가세", value=f"{krw * 0.23}원")
    embed.add_field(name="예상 총가격", value=f"{plus_duty}원")
    embed.set_footer(text="show me the money by yoonj#0492", icon_url="https://spng.pngfind.com/pngs/s/31-317340_stack-of-money-png-pile-of-money-transparent.png")
    await ctx.send(embed=embed)

@client.command(name='원유로')  # 환전값
async def KRWEUR(ctx, euros):
    api_url = "https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWEUR"
    response = requests.get(api_url)

    data = response.json()

    for j in data:
        price = j['basePrice']

    krw = int(price) * int(euros)
    plus_duty = krw + (krw * 0.23)
    embed = discord.Embed(title=f"€{euros}은 현재 환율로 {krw}원 입니다.", color=0xA71313)
    embed.add_field(name="예상 관부가세", value=f"{krw * 0.23}원")
    embed.add_field(name="예상 총가격", value=f"{plus_duty}원")
    embed.set_footer(text="show me the money by yoonj#0492", icon_url="https://spng.pngfind.com/pngs/s/31-317340_stack-of-money-png-pile-of-money-transparent.png")
    await ctx.send(embed=embed)


client.run(bot_token)
