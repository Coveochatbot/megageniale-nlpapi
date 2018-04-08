from configparser import ConfigParser
from flask import Flask
import os
app = Flask(__name__)


class Config:
    def __init__(self):
        parser = ConfigParser()
        file_list = parser.read('config.ini')
        if not file_list:
            raise ValueError('No config file found in path ' + app.instance_path)
        for name in parser.sections():
            self.__dict__.update(parser.items(name))

    def get(self, name):
        return self.__getattribute__(name)


config = Config()

