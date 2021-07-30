import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '청아 ')

@client.command()
async def 안녕(ctx):
    await ctx.send('안녕여행자')
    
@client.command()
async def 원신유튜브(ctx):
    await ctx.send('https://www.youtube.com/channel/UCcum1rCJ5GJeQ_xv0xrohqg')
    
@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="게임"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)


client.run(os.environ['token'])
