import disnake


class Item:
    def __init__(self):
        super().__init__()

    @staticmethod
    def button(callback=None, **kwargs):
        button = disnake.ui.Button(**kwargs)
        if callback is not None:
            button.callback = callback
        return button


class View(disnake.ui.View):
    def __init__(self, check, item_list=None, **kwargs):
        super().__init__(**kwargs)
        if item_list is not None:
            for x in item_list:
                self.add_item(x)
        self.interaction_check = check


class Interaction:
    def __init__(self, inter: disnake.ApplicationCommandInteraction):
        super().__init__()
        self.inter = inter

    async def check_user(self, interaction: disnake.MessageInteraction):
        if interaction.author != self.inter.author:
            await interaction.response.send_message("<:wrong:927464543016345641> 명령어를 실행한 유저만 사용할 수 있습니다.",
                                                    ephemeral=True)
            return False
        else:
            return True

    async def check_permission(self, interaction: disnake.MessageInteraction):
        if interaction.author != self.inter.author:
            await interaction.response.send_message("<:wrong:927464543016345641> 이 동작을 실행할 권한이 없습니다.",
                                                    ephemeral=True)
            return False
        else:
            return True
