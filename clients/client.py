from services import *

bot = commands.Bot(command_prefix = '/', intents = discord.Intents.all())
slash = SlashCommand(bot, sync_commands = True)

@bot.event
async def on_ready():
    DiscordComponents(bot)
    print(bot.user)
    
def func_event():
    folder = 'events'
    for file in os.listdir(f'./{folder}'):
        if file.endswith('.py'):
            bot.load_extension(f'{folder}.{file[:-3]}')

def func_command():
    folder = 'commands'
    for file in os.listdir(f'./{folder}'):
        if file.endswith('.py'):
            bot.load_extension(f'{folder}.{file[:-3]}')

def run():
    func_event()
    func_command()
    
    bot.run(BOT_TOKEN)