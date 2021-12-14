from discord import colour
from services import *

class Messages(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('>> EVENT: messages Loaded')

    @commands.Cog.listener()
    async def on_message(self, event: discord.message.Message):
        page = discord.Embed(title = 'CRUNZEX', colour = discord.Colour.blurple())
        await event.reply(embed = page)
        
def setup(bot:commands.Bot):
    bot.add_cog(Messages(bot))