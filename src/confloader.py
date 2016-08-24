import json
import os


class PellConfig:

    def __init__(
            self,
            loadconf=True,  # Load the config file
            loadrc=False,  # Load the rc file
            confpath=os.path.expanduser("~")+'/.pell.conf',  # Path to the conf file
            rcpath=os.path.expanduser("~")+'/.pellrc'):  # Path to the rc file

        self.__config = {}  # Contains the keys and values for the options.
        self.__defconfpath = "/etc/pell/pell.conf"  # Default conf path
        self.__defrcpath = "/etc/pell/pellrc"  # Default rc path
        self.__confpath = confpath
        self.__rcpath = rcpath

        if loadconf == True:
            self.parse_conf()

    # Returns the value of an option or a default if the option doesn't exist.
    def get_option(self, optname, defvalue):
        if optname in self.__config:
            return self.__config[optname]
        else:
            return defvalue

    # Sets an option to the specified value
    def set_option(self, optname, value):
        pass

    # Parses the rc file set in the initialiser.
    # If execrc is set to True, execute any functions inside the rc file.
    def parse_rc(self, execrc=False):
        pass

    # Parses the conf file set in the initialiser with the json module.
    def parse_conf(self):
            try:
                if os.path.isfile(self.__confpath):
                    jsonfile = open(self.__confpath, "r")
                elif os.path.isfile(self.__defconfpath):
                    jsonfile = open(self.__defconfpath, "r")
                else:
                     print("No valid config file found.")
                     return
                self.__config = json.load(jsonfile)
            except (ValueError,IOError) as e:
                print("Unable to load config file at:", e)

    # Return the config as a dictionary.
    def as_dict(self):
        return self.__config
