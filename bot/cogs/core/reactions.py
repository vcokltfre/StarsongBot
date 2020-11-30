import discord
from yaml import safe_load
from discord.ext import commands

from bot.bot import Bot

with open("./bot/cogs/core/config.yml") as f:
    config = safe_load(f)
    roles = config["reactions"]
    message = config["message"]


class Reactions(commands.Cog):
    """A cog for reaction roles"""

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.guild = self.bot.get_guild(378424432827301888)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if payload.message_id == message:
            if payload.emoji.id in roles:
                roleadd = self.guild.get_role(roles[payload.emoji.id])
                member = self.guild.get_member(payload.user_id)

                await member.add_roles(roleadd)


def setup(bot: Bot):
    bot.add_cog(Reactions(bot))
