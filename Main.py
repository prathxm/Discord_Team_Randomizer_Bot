#Modules
import discord 
import random
import math
import os
from KeepAlive import keep_alive
#Functions
client = discord.Client()
@client.event 
async def distribution(n,m,message):#m=number of teams,n=number of participants
              def check(mem):
                return mem.author.id == message.author.id
              profile=[]
              pool=[]
              '''if che.startswith('n'or'N'):
                for i in range(1,n+1):
                  name="Player"+str(i)
                  profile.append(name)
                pool=profile'''
              s_final=''
              for i in range(n):
                            await message.channel.send('Enter name')
                            lol = await client.wait_for("message",check=check)
                            lol1=str(lol.content)
                            pool.append(lol1)
              if(len(pool)%2!=0):
                            pool.append('-')
                            n+=1
              dist=math.ceil(n/m)
              players=dist*m
              if(len(pool)!=players):
                for i in range(players-len(pool)):
                  pool.append("-")
                  n+=1
              for i in range(m):
                            s_final=s_final+"**Team** \n **---------** \n"
                            for j in range(dist):
                                          slct=random.randrange(n)
                                          s_final=s_final+pool[slct]+"\n"
                                          pool.remove(pool[slct])
                                          n-=1
              return(s_final)



@client.event
async def on_ready():
  print("Bot Online Bitches")
@client.event
async def on_message(message):
  if message.content.startswith('/tr'):
    def check(mem):
      return mem.author.id == message.author.id
    await message.channel.send('Hello {.author} \n Enter number of players'.format(message))
    msg = await client.wait_for('message',check=check)
    await message.channel.send('{.author} \n Enter number of teams'.format(message))
    msg2 = await client.wait_for('message',check=check)
    '''await message.channel.send('{.author} \n Do you want to add names'.format(message))
    msg3 = await client.wait_for('message',check=check)'''
    n = int(msg.content)
    m = int(msg2.content)
    #che= str(msg3.content)
    answer = await distribution(n,m,message)
    await message.channel.send(answer)
keep_alive()
client.run(os.getenv('Token'))

                       
