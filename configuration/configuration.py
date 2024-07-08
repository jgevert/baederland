import configparser


def get_config(file: str) -> configparser.ConfigParser:
    """
    This function accepts a file locatgion as string and loads the information into a configparser object
    :param file: file location as string
    :return: configparser.ConfigParser
    """
    config = configparser.ConfigParser()
    config.read(file)
    return config


def make_dict(configuration: configparser.ConfigParser) -> dict:
    """
    This function accepts a configparser object and transforms the data into a dictionary
    :param configuration: configparser.>ConfigParser object
    :return: dictionary
    """
    configurations_dict = dict()
    sections = configuration.sections()
    for section in sections:
        configurations_dict[section] = dict()
        options = configuration.options(section)
        for option in options:
            configurations_dict[section][option] = configuration.get(section, option)
    return configurations_dict


def run(file: str) -> dict:
    """
    Run function for logic. Orchestrates the get_config and make_dict function
    :param file: file location as string
    :return: dictionary
    """
    return make_dict(get_config(file))

