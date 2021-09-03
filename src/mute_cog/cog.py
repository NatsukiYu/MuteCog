import os
from logging import getLogger

import discord
from discord import Member
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

guild_ids = os.environ.get('guild_ids')
if guild_ids is not None:
    guild_ids = list(map(lambda x: int(x), guild_ids.split(',')))

logger = getLogger(__name__)


class MuteCog(commands.Cog):
    """サーバーミュートを設定・解除するCog"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @cog_ext.cog_slash(name='mute', description='mute member', guild_ids=guild_ids)
    async def mute(self, ctx: SlashContext, member: Member):
        logger.debug(f'mute {member.display_name}')
        voice: discord.VoiceState = member.voice
        if voice is None:
            await ctx.send(f'{member.display_name}は通話中ではありません', hidden=True)
            return
        await member.edit(mute=True)
        await ctx.send(f'{member.display_name}をミュートしました', hidden=True)

    @cog_ext.cog_slash(name='unmute', description='unmute member', guild_ids=guild_ids)
    async def unmute(self, ctx: SlashContext, member: Member):
        logger.debug(f'unmute {member.display_name}')
        voice: discord.VoiceState = member.voice
        if voice is None:
            await ctx.send(f'{member.display_name}は通話中ではありません', hidden=True)
            return
        await member.edit(mute=False)
        await ctx.send(f'{member.display_name}をミュート解除しました', hidden=True)


def setup(bot):
    return bot.add_cog(MuteCog(bot))
