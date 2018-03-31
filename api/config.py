from configparser import ConfigParser
import os


class Config:
    def __init__(self):
        parser = ConfigParser()
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, 'config.ini')
        found = parser.read(abs_file_path)
        if not found:
            raise ValueError('No config file found!')
        for name in parser.sections():
            self.__dict__.update(parser.items(name))

    def get(self, name):
        return self.__getattribute__(name)


config = Config()

