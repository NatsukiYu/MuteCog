from discord.ext import commands
from discord_slash import SlashCommand

bot = commands.Bot(command_prefix='!')
slash = SlashCommand(bot, sync_commands=True)
bot.load_extension('mute_cog')  # <1>
bot.run('<bot token>')  # <2>
