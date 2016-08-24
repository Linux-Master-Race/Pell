import json

class PellConfig:

    def __init__(
            self,
            loadconf=True,  # Load the config file
            loadrc=False,  # Load the rc file
            confpath='/home/misero/.config/pell.conf',  # Path to the conf file
            rcpath='~/.pellrc'):  # Path to the rc file

        self.__config = {}  # Contains the keys and values for the options.
        self.__defconfpath = confpath  # Default conf path
        self.__defrcpath = rcpath  # Default rc path


    def getNode(self, section, name):
        try:
            return self.__config[section][name]
        except:
            return ""

    # Parses the conf file set in the initialiser with the json module.
    def parse_conf(self):
        with open(self.__defconfpath, 'r') as f:
            self.__config = json.load(f)

    # Return the config as a dictionary.
    def as_dict(self):
        return self.__config
