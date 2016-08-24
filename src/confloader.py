import json


class PellConfig:

    def __init__(
            self,
            loadconf=True,
            loadrc=False,
            rcpath='~/.pellrc)',
            confpath='~/.pell.conf'):

        self.__config = {}

    def get_option(self, optionname, defvalue):
        pass

    def set_option(self, optionname, value):
        pass

    def parse_rc(self, executecode=False):
        pass

    def parse_conf(self):
        pass
