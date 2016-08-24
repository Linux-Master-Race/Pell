import json


class PellConfig:

    def __init__(
            self,
            loadconf=True,  # Load the config file
            loadrc=False,  # Load the rc file
            confpath='~/.config/pell.conf',  # Path to the conf file
            rcpath='~/.config/pellrc'):  # Path to the rc file

        self.__config = {}  # Contains the keys and values for the options.
        self.__defconfpath = "/etc/pell/pell.conf"  # Default conf path
        self.__defrcpath = "/etc/pell/pellrc"  # Default rc path

    # Returns the value of an option or a default if the option doesn't exist.
    def get_option(self, optname, defvalue):
        pass

    # Sets an option to the specified value
    def set_option(self, optname, value):
        pass

    # Parses the rc file set in the initialiser.
    # If execrc is set to True, execute any functions inside the rc file.
    def parse_rc(self, execrc=False):
        pass

    # Parses the conf file set in the initialiser with the json module.
    def parse_conf(self):
        pass

    # Gets the path to the rc file.
    def get_rc_path(self):
        pass

    # Gets the path to the conf file.
    def get_conf_path(self):
        pass

    # Sets the path to the rc file.
    def set_rc_path(self, rcpath):
        pass

    # Sets the path to the conf file.
    def set_conf_path(self, confpath):
        pass

    # Return the config as a dictionary.
    def as_dict(self):
        return self.__config
