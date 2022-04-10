import argparse
import threading
import sys
import os

import discord
from discord.ext import commands
from discord.utils import get

import conf.config as config
from manager.logger import Logger, Level

def main():

    parser = argparse.ArgumentParser(add_help=True, description="")
    args = parser.parse_args()

    Logger.Get()
    Logger.Get().Initialize("CC", "CC.log", level=Level.DEBUG)

    config.PATH_ROOT = os.path.abspath("..")
    if not os.path.exists(f"{config.PATH_ROOT}{os.sep}Configuration"):
        os.mkdir(f"{config.PATH_ROOT}{os.sep}Configuration")

    Logger.Get().debug(f"Using {config.PATH_ROOT = }")
    Logger.Get().Add("UI", "ui.log")
    Logger.Get().UI.debug("test")
    Logger.Get().UI.Add("CUI")
    Logger.Get().UI.CUI.debug("another test")
    log = Logger.Get().UI
    log.debug("Local instance")
    log.CUI.debug("Nested local")

if __name__ == "__main__":
    main()