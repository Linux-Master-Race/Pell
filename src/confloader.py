import json


class PellConfig:

    def __init__(
            self,
            loadconf=True,
            loadrc=False,
            rcpath='~/.pellrc',
            confpath='~/.pell.conf'):

        self.__config = {}
        self.__defconfpath = "/etc/pell/pell.conf"
        self.__defrcpath = "/etc/pell/pellrc"

    def get_option(self, optname, defvalue):
        pass

    def set_option(self, optname, value):
        pass

    def parse_rc(self, execrc=False):
        pass

    def parse_conf(self):
        pass

    def set_rc_path(self, rcpath):
        pass

    def set_conf_path(self, confpath):
        pass

    def as_dict(self):
        return self.__config

