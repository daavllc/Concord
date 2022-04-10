from utils.logging import Level
from utils.logging import Logger as log

class Logger:
    __instance = None
    """
        Logger context manager
    """

    class Group:
        def __init__(self, file: str, level: Level = Level.DEBUG, clevel: Level = None, flevel: Level = None, cout: bool = True, fout: bool = True, logname: str = ""):
            self.logger = log(logname, file, level, clevel, flevel, cout, fout)

        def Add(self, name: str, file: str = None, level: Level = None, clevel: Level = None, flevel: Level = None, cout: bool = None, fout: bool = None):
            if file is None:
                file = self.logger.file
            if level is not None:
                if clevel is None:
                    clevel = level
                if flevel is None:
                    flevel = level
            else:
                if clevel is None:
                    clevel = self.logger.cLevel
                if flevel is None:
                    flevel = self.logger.fLevel
            if cout is None:
                cout = self.logger.cout
            if fout is None:
                fout = self.logger.fout
            super(Logger.Group, self).__setattr__(name, Logger.Group(file, level, clevel, flevel, cout, fout, self.logger.name + '.' + name))

        def debug(self, message: str):
            self.logger.debug(message)

        def info(self, message: str):
            self.logger.info(message)

        def warn(self, message: str):
            self.logger.warn(message)

        def error(self, message: str):
            self.logger.error(message)

        def critical(self, message: str):
            self.logger.critical(message)

    @staticmethod
    def Get():
        if Logger.__instance is None:
            Logger.__instance = Logger()
        return Logger.__instance

    def __init__(self):
        if Logger.__instance is not None:
            raise Exception("Logger manager attempted re-init")

    def Initialize(self, name: str, file: str, level: Level = Level.DEBUG, clevel: Level = None, flevel: Level = None, cout: bool = True, fout: bool = True):
        if level is None:
            if clevel is None:
                clevel = Level.DEBUG
            if flevel is None:
                flevel = Level.DEBUG
        else:
            if clevel is None:
                clevel = level
            if flevel is None:
                flevel = level
        self.logger = log(name, file, level, clevel, flevel, cout, fout)

    def Add(self, name: str, file: str, level: Level = Level.DEBUG, clevel: Level = None, flevel: Level = None, cout: bool = None, fout: bool = None):
        if file is None:
            file = self.logger.file
        if level is None:
            if clevel is None:
                clevel = self.logger.cLevel
            if flevel is None:
                flevel = self.logger.fLevel
        if cout is None:
            cout = self.logger.cout
        if fout is None:
            fout = self.logger.fout
        super(Logger, self).__setattr__(name, self.Group(file, level, clevel, flevel, cout, fout, self.logger.name + '.' + name))

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warn(self, message: str):
        self.logger.warn(message)

    def error(self, message: str):
        self.logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)