import discord
import os


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        return


    async def on_message(self,message):
        if message.author==client.user:
            return
        print("i breathe")
        global PrevMessage
        if PrevMessage is not None:
            await PrevMessage.delete()
        PrevMessage = await message.channel.send("im being abused")


PrevMessage=None

















































intents=discord.Intents.all()
client = MyClient(intents=intents)
TokenFile=open('our token',"r")
token=TokenFile.readline()
client.run(token)




















