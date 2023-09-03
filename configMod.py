import configparser

def set_public_key(pathConfig, userKey):
    config = configparser.ConfigParser()
    config.read(pathConfig)
    config['main']['public-key'] = userKey
    with open(pathConfig, 'w') as configfile:
        config.write(configfile)

def get_public_key(pathConfig):
    config = configparser.ConfigParser()
    config.read(pathConfig)
    return config['main']['public-key']


