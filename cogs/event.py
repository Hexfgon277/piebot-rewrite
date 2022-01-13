import disnake
from disnake.ext import commands
from color import Color

import colorlog

logger = colorlog.getLogger('pie')


def setup(bot):
    bot.add_cog(Event(bot))


class Event(commands.Cog, name='이벤트'):
    def __init__(self, _bot):
        self.bot = _bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.BadArgument):
            embed = disnake.Embed(title="<:wrong:927464543016345641> 잘못된 사용법이에요.",
                                  description=f"**올바른 사용법**:\n"
                                              f"> {ctx.command.usage.format(ctx.prefix, pref=ctx.prefix)}",
                                  color=0x9BDDFF
                                  )
            embed.set_footer(text=f"<>는 꼭 입력해야하는 값, []는 입력하지 않아도 되는 값입니다.")
            await ctx.reply(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply("<:wrong:927464543016345641> 이 명령을 실행하시려면 **관리자 권한**이 필요해요.")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply("<:wrong:927464543016345641> 봇이 이 명령어를 실행할 권한이 없습니다. 봇의 역할을 확인해주세요.")
        else:
            embed = disnake.Embed(title="Error", description=f"```{error}```", color=Color.RED)
            logger.error(error)
            await ctx.reply(embed=embed)
