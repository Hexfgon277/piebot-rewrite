from disnake.ext import commands

from color import Color
from bot_ui import *
from converter import time_converter


def setup(bot):
    bot.add_cog(Admin(bot))


class Admin(commands.Cog, name='관리'):
    def __init__(self, _bot):
        self.bot = _bot

    @commands.slash_command(name="purge")
    async def _purge(self, inter, amount: int):
        """입력한 수만큼의 메세지를 삭제해요."""

        async def delete_message(_interaction):
            await msg.delete()

        if 0 < amount < 100:
            await inter.response.send_message("<:info:927499124763426826> 잠시 기다려주세요..")
            purge = await inter.channel.purge(limit=amount)
            button = Item.button(callback=delete_message, label="메시지 닫기", emoji="🔐")
            view = View(check=Interaction(inter).check_user, item_list=[button])
            embed = disnake.Embed(title="<:check:927499139284074506> 완료!",
                                  description=f"{len(purge)}개의 메세지를 삭제하였습니다!",
                                  color=Color.GREEN)
            embed.set_footer(text=inter.author, icon_url=inter.author.avatar)
            msg = await inter.channel.send(embed=embed, view=view)
        else:
            await inter.response.send_message("<:wrong:927464543016345641> 1부터 99까지의 숫자만 입력하실 수 있어요.",
                                              ephemeral=True)

    @commands.slash_command(name="ban")
    async def _ban(self, inter, user: disnake.Member, reason: str):
        """선택한 유저를 서버에서 차단시켜요."""

        async def ban(_interaction):
            await msg.edit(view=None)
            await user.ban(reason=reason)
            finished_embed = disnake.Embed(
                title="<:check:927499139284074506> 완료!",
                description=f"{user}의 처벌을 성공적으로 완료하였습니다!",
                color=0x00FF00)
            finished_embed.set_footer(text=inter.author, icon_url=inter.author.avatar)
            await _interaction.response.send_message(embed=finished_embed)

        async def cancel(_interaction):
            await msg.edit(view=None)
            await _interaction.response.send_message("<:wrong:927464543016345641> 취소되었습니다.")

        o_button = disnake.ui.Button(label="네", style=disnake.ButtonStyle.green)
        o_button.callback = ban
        x_button = disnake.ui.Button(label="아니오", style=disnake.ButtonStyle.danger)
        x_button.callback = cancel
        embed = disnake.Embed(title="처벌",
                              description=f"{user.mention}를 다음과 같은 이유로 처벌하시겠습니까?",
                              color=Color.MAIN)
        embed.add_field(name="처벌 유형", value="밴(차단)", inline=False)
        embed.add_field(name="사유", value=reason, inline=False)
        embed.add_field(name="관리자", value=inter.author, inline=False)
        await inter.response.send_message("<:info:927499124763426826> 권한이 확인되었습니다.")
        msg = await inter.followup.send(
            embed=embed,
            view=View(
                check=Interaction(inter).check_user,
                item_list=[o_button, x_button])
        )

    @commands.slash_command(name="kick")
    async def _kick(self, inter, user: disnake.Member, reason: str):
        """선택한 유저를 서버에서 추방시켜요."""

        async def kick(_interaction):
            await msg.edit(view=None)
            await user.kick(reason=reason)
            finished_embed = disnake.Embed(
                title="<:check:927499139284074506> 완료!",
                description=f"{user}의 처벌을 성공적으로 완료하였습니다!",
                color=0x00FF00)
            finished_embed.set_footer(text=inter.author, icon_url=inter.author.avatar)
            await _interaction.response.send_message(embed=finished_embed)

        async def cancel(_interaction):
            await msg.edit(view=None)
            await _interaction.response.send_message("<:wrong:927464543016345641> 취소되었습니다.")

        o_button = disnake.ui.Button(label="네", style=disnake.ButtonStyle.green)
        o_button.callback = kick
        x_button = disnake.ui.Button(label="아니오", style=disnake.ButtonStyle.danger)
        x_button.callback = cancel
        embed = disnake.Embed(title="처벌",
                              description=f"{user.mention}를 다음과 같은 이유로 처벌하시겠습니까?",
                              color=Color.MAIN)
        embed.add_field(name="처벌 유형", value="추방(킥)", inline=False)
        embed.add_field(name="사유", value=reason, inline=False)
        embed.add_field(name="관리자", value=inter.author, inline=False)
        await inter.response.send_message("<:info:927499124763426826> 권한이 확인되었습니다.")
        msg = await inter.followup.send(
            embed=embed,
            view=View(
                check=Interaction(inter).check_user,
                item_list=[o_button, x_button])
        )

    @commands.slash_command(name="timeout")
    async def _timeout(self, inter, user: disnake.Member, duration: int or float, reason: str):
        """선택한 유저를 입력한 시간동안 타임아웃시켜요. duration은 초단위로 사용됩니다. ex) 30 = 30초, 60 = 1분"""

        async def timeout(_interaction):
            await msg.edit(view=None)
            await user.timeout(duration=float(duration), reason=reason)
            finished_embed = disnake.Embed(
                title="<:check:927499139284074506> 완료!",
                description=f"{user}의 처벌을 성공적으로 완료하였습니다!",
                color=0x00FF00)
            finished_embed.set_footer(text=inter.author, icon_url=inter.author.avatar)
            await _interaction.response.send_message(embed=finished_embed)

        async def cancel(_interaction):
            await msg.edit(view=None)
            await _interaction.response.send_message("<:wrong:927464543016345641> 취소되었습니다.")

        o_button = disnake.ui.Button(label="네", style=disnake.ButtonStyle.green)
        o_button.callback = timeout
        x_button = disnake.ui.Button(label="아니오", style=disnake.ButtonStyle.danger)
        x_button.callback = cancel
        embed = disnake.Embed(title="처벌",
                              description=f"{user.mention}를 다음과 같은 이유로 처벌하시겠습니까?",
                              color=Color.MAIN)
        embed.add_field(name="처벌 유형", value=f"타임아웃 ({time_converter(duration)})", inline=False)
        embed.add_field(name="사유", value=reason, inline=False)
        embed.add_field(name="관리자", value=inter.author, inline=False)
        await inter.response.send_message("<:info:927499124763426826> 권한이 확인되었습니다.")
        msg = await inter.followup.send(
            embed=embed,
            view=View(
                check=Interaction(inter).check_user,
                item_list=[o_button, x_button])
        )