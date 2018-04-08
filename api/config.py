from configparser import ConfigParser


class Config:
    def __init__(self, path):
        parser = ConfigParser()
        file_list = parser.read(path)
        if not file_list:
            raise ValueError('No config file found!')
        for name in parser.sections():
            self.__dict__.update(parser.items(name))

    def get(self, name):
        return self.__getattribute__(name)


config = Config('config.ini')

