from datetime import datetime

import disnake
import websockets as websockets
from disnake.ext import commands, tasks


def setup(bot: commands.Bot):
    bot.add_cog(Updater(bot))


class Updater(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.begin_at = datetime.utcnow()
        self.update_presence.add_exception_type(websockets.ConnectionClosedError)
        self.update_presence.start()

    def cog_unload(self):
        self.update_presence.cancel()

    @tasks.loop(seconds=30.0)
    async def update_presence(self):
        activity = disnake.Game(name=f"/도움 | {len(set(self.bot.guilds))} 서버")
        await self.bot.change_presence(activity=activity)

    @update_presence.before_loop
    async def before_update(self):
        await self.bot.wait_until_ready()