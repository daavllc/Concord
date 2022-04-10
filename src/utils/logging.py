from enum import Enum
from datetime import datetime as dt
from os import sep
from os import mkdir
from os.path import exists

import conf.config as config

class Level(Enum):
    NONE = 100
    DEBUG = 1
    INFO = 2
    WARN = 3
    ERROR = 4
    CRITICAL = 5

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def __le__(self, other) -> bool:
        return self.value <= other.value

    def __gt__(self, other) -> bool:
        return self.value > other.value

    def __ge__(self, other) -> bool:
        return self.value >= other.value

class Logger:
    def __init__(self, name: str, file: str, level: Level = Level.DEBUG, clevel: Level = None, flevel: Level = None, cout: bool = True, fout: bool = True):
        """
            Logger instance 

        Args:
            name (str): Name of the logger
            file (str): File to save logs to
            level (Level, optional): Logging level. Defaults to Level.DEBUG.
            clevel (Level, optional): Console logging level. If None, defaults to level.
            flevel (Level, optional): File logging level. If None, defauls to level.
            cout (bool, optional): Log to console. Defaults to True.
            fout (bool, optional): Log to file. Defaults to True.
        """
        self.name: str = name
        self.file: str = file
        if clevel is None:
            self.cLevel = level
        else:
            self.cLevel = clevel
        if flevel is None:
            self.fLevel = level
        else:
            self.fLevel = flevel
        self.cout: bool = cout
        self.fout: bool = fout

    def debug(self, message: str):
        self.__log(Level.DEBUG, message)

    def info(self, message: str):
        self.__log(Level.INFO, message)

    def warn(self, message: str):
        self.__log(Level.WARN, message)

    def error(self, message: str):
        self.__log(Level.ERROR, message)

    def critical(self, message: str):
        self.__log(Level.CRITICAL, message)

    def Set(self, level: Level):
        self.level = level

    def __log(self, level: Level, message: str):
        message = f"{dt.now().strftime('%Y-%m-%d %H:%M:%S')} <{self.name}> {level.name}: {message}"

        if self.fout and level >= self.fLevel:
            try:
                with open(f"{config.PATH_ROOT}{sep}logs{sep}{self.file}", "a") as f:
                    f.write(message + "\n")
            except FileNotFoundError:
                if not exists(f"{config.PATH_ROOT}{sep}logs"):
                    mkdir(f"{config.PATH_ROOT}{sep}logs")
                with open(f"{config.PATH_ROOT}{sep}logs{sep}{self.file}", "w") as f:
                    f.write(message + "\n")

        if self.cout and level >= self.cLevel:
            print(message)