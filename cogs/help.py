from disnake.ext import commands

from config import Config
from bot_ui import *


def setup(bot):
    bot.add_cog(Help(bot))


class Help(commands.Cog, name='도움'):
    def __init__(self, _bot):
        self.bot = _bot

    @commands.slash_command(name="초대", usage="{}초대")
    async def _invite(self, inter):
        """
        파이봇을 다른 서버에 초대할 수 있어요!
        """
        embed = disnake.Embed(title="파이봇 초대하기",
                              description=f"[이곳]({Config.core['invite_link']})에 들어가거나 아래 버튼을 눌러 봇을 초대하세요.")
        button = Item.button(label="파이봇 초대하기", style=disnake.ButtonStyle.url, url=Config.core['invite_link'])
        await inter.response.send_message(embed=embed, view=View(check=None, item_list=[button]))

    @commands.slash_command(name="서포트", usage="{}서포트")
    async def _support(self, inter):
        """
        파이봇의 공식 서버에 참여할 수 있는 명령어입니다.
        이곳에서 봇과 관련된 많은 도움을 받아가실 수 있어요!
        """
        embed = disnake.Embed(title="파이봇 서포트 서버",
                              description=f"[이곳]({Config.core['server_link']})에 들어가거나 아래 버튼을 눌러 파이봇 공식 서버에 참여하세요.")
        button = Item.button(label="서포트 서버 참여하기", style=disnake.ButtonStyle.url, url=Config.core['server_link'])
        await inter.response.send_message(embed=embed, view=View(check=None, item_list=[button]))
