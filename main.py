import disnake
import colorlog

from bot import PieBot
from config import Config


logger = colorlog.getLogger('pie')
bot = PieBot(command_prefix=Config.core['test_prefix'] if Config.core['testmode'] == 1 else Config.core['prefix'],
             help_command=None,
             allowed_mentions=disnake.AllowedMentions(everyone=False, users=True, roles=False, replied_user=False),
             intents=disnake.Intents.all(),
             test_guilds=[835871330502705182, 754876579695296564, 795144676814487553])


@bot.event
async def on_ready():
    logger.info(f'Log in: {bot.user}')
    bot.ready_extensions()


@bot.event
async def on_message(message: disnake.Message):
    ctx = await bot.get_context(message)
    if message.author.bot:
        return
    await bot.invoke(ctx)


@bot.before_slash_command_invoke
async def before_slash_command_invoke(inter):
    logger.debug(
        f"({inter.author.id}) {inter.author}: /{inter.data.name} {' '.join(str(x.value) for x in inter.data.options)}"
    )


@bot.before_invoke
async def before_invoke(inter):
    logger.debug(f"({inter.author.id}) {inter.author}: {inter.message.content}")


def setup_logger():
    logger.setLevel('DEBUG')
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter('{log_color}[{asctime} {levelname}] {message}', '%y.%m.%d %H:%M:%S', style='{'))
    logger.addHandler(handler)
    logger.info("Logging Activated")


if __name__ == '__main__':
    setup_logger()
    bot.run(Config.core['test_token'] if Config.core['testmode'] == 1 else Config.core['token'])
