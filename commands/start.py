from services import *

class Start(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('>> COMMAND: start Loaded')
        
    @cog_ext.cog_slash(
        name = 'start',
        description = 'example: start command'
    )
    async def _start(self, event: SlashContext):
        await event.reply('CRUNZEX', delete_after = 30.0)
        
def setup(bot:commands.Bot):
    bot.add_cog(Start(bot))