import sys

from loguru import logger as _logger

logger = _logger

default_format = (
    "<g>{time:MM-DD HH:mm:ss}</g> "
    "[<lvl>{level}</lvl>] "
    "<c><u>{name}</u></c> | "
    "<c>{function}:{line}</c>| "
    "{message}")

logger.remove()

logger_id = logger.add(sys.stdout,
                       colorize=True,
                       diagnose=False,
                       format=default_format)
# logger.add(sink="logs/{time}.log",
#            rotation="00:00",
#            retention='1 week',
#            enqueue=True,
#            diagnose=False,
#            level="SUCCESS",
#            format=default_format,
#            encoding='utf-8'
#            )
