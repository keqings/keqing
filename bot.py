import discord
from discord.ext import commands
import os

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="게임"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

client = commands.Bot(command_prefix = '청아 ')

@client.command()
async def 안녕(ctx):
    await ctx.send('안녕여행자')

@client.command()
async def 도움말(ctx) :
    embed = discord.Embed(title = "도움말",
    description = "리월칠성 청이 사용하는 방법입니다. \n\n**청아 안녕**\청이랑 인사할 수 있습니다.\n\n**청아 원신**\n원신 공식 유튜브입니다.\n\n**청아 지도**\n티바트 지역 전체 맵을 볼 수 있습니다.\n\n**청아 롤패치노트**\n롤 패치노트를 볼 수 있습니다.\n\n**청아 원신나무위키**\n원신 나무위키입니다.", color = 0x62c1cc)   
    embed.set_footer(text = f"{ctx.message.author.name}", icon_url = ctx.message.author.avatar_url)
    await ctx.send(embed = embed)

@client.command()
async def 원신(ctx):
    await ctx.send('https://www.youtube.com/channel/UCcum1rCJ5GJeQ_xv0xrohqg')

@client.command()
async def 지도(ctx):
    await ctx.send('https://webstatic-sea.mihoyo.com/app/ys-map-sea/index.html?lang=ko-kr#/map/2?shown_types=5,194&center=82.00,-1169.00&zoom=-2.00')

@client.command()
async def 롤패치노트(ctx):
    await ctx.send('https://kr.leagueoflegends.com/ko-kr/news/tags/patch-notes')   

@client.command()
async def 원신나무위키(ctx):
    await ctx.send('https://namu.wiki/w/%EC%9B%90%EC%8B%A0')   
                          
client.run(os.environ['token'])
