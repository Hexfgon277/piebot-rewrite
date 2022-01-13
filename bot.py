import os
import colorlog
from disnake.ext import commands

logger = colorlog.getLogger('pie')


class PieBot(commands.AutoShardedBot):
    """파이봇 AutoShardedBot"""
    __version__ = "0.0.1b"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def extension_load(self, file):
        try:
            self.load_extension(file)
        except commands.ExtensionAlreadyLoaded:
            self.reload_extension(file)

    def ready_extensions(self):
        for f in os.listdir('cogs'):
            if f.endswith('.py'):
                try:
                    self.extension_load(f'cogs.{f[:-3]}')
                    logger.info(f"Extension {f[:-3]} loaded")
                except Exception as e:
                    logger.error(f"Extension {f[:-3]} load failed")
                    logger.error(f"Error: {e}")
        self.extension_load('jishaku')
        logger.info('Extension load finished')
