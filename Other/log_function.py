import logging


def log():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('discord')
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)