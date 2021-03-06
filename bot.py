import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = ';')
    
@client.command()
async def 안녕(ctx):
    await ctx.send('안녕 여행자')

@client.command()
async def 도움말(ctx) :
   embed=discord.Embed(title="", description="각청봇 사용법입니다. ;뒤에 입력해주세요.", color=0x0055ff)
   embed.set_author(name="각청", icon_url="https://pbs.twimg.com/profile_images/1325830385326907394/qBBNn2Zd_400x400.jpg")
   embed.add_field(name="안녕", value="각청과 인사할 수 있습니다.", inline=False)
   
   embed.add_field(name="원신", value="원신에 관한 모든 것!", inline=True)
   embed.add_field(name="지도", value="티바트 모든 맵을 볼 수 있습니다.", inline=True)
   embed.add_field(name="캐릭터", value="플레이어블 캐릭터들을 볼 수 있습니다.", inline=True)
   embed.add_field(name="무기", value="원신에 나오는 모든 무기를 찾아볼 수 있습니다.", inline=True)
   embed.add_field(name="롤패치", value="롤 패치노트를 볼 수 있습니다.", inline=True)
   embed.add_field(name="전적", value="롤 전적검색 사이트로 갑니다!", inline=True)
   embed.add_field(name="에펙패치", value="에이펙스 패치노트를 볼 수 있습니다.", inline=True)
   
   embed.set_footer(text="추가하고 싶은 내용을 말해주세요.")
   await ctx.send(embed=embed)

@client.command()
async def 원신(ctx):
    await ctx.send('https://www.youtube.com/channel/UCcum1rCJ5GJeQ_xv0xrohqg')

@client.command()
async def 지도(ctx):
    await ctx.send('https://genshin.gamedot.org/?mid=genshinmaps')

@client.command()
async def 캐릭터(ctx):
    await ctx.send('https://namu.wiki/w/%ED%8B%80:%EC%9B%90%EC%8B%A0%20%ED%94%8C%EB%A0%88%EC%9D%B4%EC%96%B4%EB%B8%94%20%EC%BA%90%EB%A6%AD%ED%84%B0')
   
@client.command()
async def 무기(ctx):
    await ctx.send('https://namu.wiki/w/%EC%9B%90%EC%8B%A0/%EB%AC%B4%EA%B8%B0')
   
@client.command()
async def 롤패치(ctx):
    await ctx.send('https://kr.leagueoflegends.com/ko-kr/news/tags/patch-notes')   
    
@client.command()
async def 에펙패치(ctx):
    await ctx.send('https://www.ea.com/ko-kr/games/apex-legends/news#game-updates')  

@client.command()
async def 전적 (ctx):
    await ctx.send('https://www.op.gg/l=ko_KR')
    
@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="업무중 ;도움말))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)


client.run(os.environ['token'])
