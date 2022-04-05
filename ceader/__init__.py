#                    _                _
#   ___ ___ _ __ ___| |__  _ __ ___  (_) ___
#  / __/ _ \ '__/ _ \ '_ \| '__/ _ \ | |/ _ \
# | (_|  __/ | |  __/ |_) | | |  __/_| | (_) |
#  \___\___|_|  \___|_.__/|_|  \___(_)_|\___/
#
#Proprietary software created by CEREBRE.
#© CEREBRE, USA. All rights reserved.
#Visit us at: https://www.cerebre.io
import logging
import os
import sys

import matplotlib

# Set the backend to prevent warnings about GUIs being opened from a thread
# other than the main thread and allow to use .renderer
# also setting this in here because this gets execute before all other stuff
matplotlib.use("Agg")

# log level
LOG_LEVEL = os.environ.get("LOG_LEVEL", "debug").upper()


def get_logger() -> logging.Logger:
    """
    utility function to get a unified logger for the whole project
    """
    logging.setLoggerClass(logging.Logger)
    logger = logging.getLogger("ceader")

    logger.setLevel(LOG_LEVEL)
    if not logger.hasHandlers():
        # we need to manually set to stdout
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt="[%(asctime)s] [%(levelname)s] <%(name)s> %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
