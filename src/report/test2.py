#!/usr/bin/python3
from os import path, makedirs
import importlib
import logging
import json
import sys

log = logging.getLogger('test')

COLORS = {'DEBUG': 'cyan', 'INFO': 'green', 'WARNING': 'yellow', 'ERROR': 'red', 'CRITICAL': 'red', }

NO_COLORS = {'DEBUG': '', 'INFO': '', 'WARNING': '', 'ERROR': '', 'CRITICAL': '', }

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

stream = sys.stdout
isatty = stream.isatty()
console_hdlr = logging.StreamHandler(stream)

def get_log_colors(theme_color=None):
    """Return a tuple containing the log format string and a log color dict"""
    if theme_color == 'light':
        text_color_theme = 'white'
    elif theme_color == 'dark':
        text_color_theme = 'black'
    else:  # Anything else produces nocolor
        return '%(name)-25.25s%(reset)s %(message)s%(reset)s', NO_COLORS

    return f'%(name)-25.25s%(reset)s %({text_color_theme})s%(message)s%(reset)s', COLORS

def format_logs(formatter=None, theme_color=None):
    """
    You may either use the formatter parameter to provide your own
    custom formatter, or the theme_color parameter to use the
    built in color scheme formatter.
    """
    if formatter:
        console_hdlr.setFormatter(formatter)
    # if isatty and not True:
    elif isatty:
        from colorlog import ColoredFormatter  # noqa
        log_format, colors_dict = get_log_colors(theme_color)
        color_formatter = ColoredFormatter(
            "%(asctime)s %(log_color)s%(levelname)-8s%(reset)s " + log_format,
            datefmt="%H:%M:%S",
            reset=True,
            log_colors=colors_dict,
        )
        console_hdlr.setFormatter(color_formatter)
    else:
        console_hdlr.setFormatter(logging.Formatter("%(asctime)s %(levelname)-8s %(name)-25s %(message)s"))
    root_logger.addHandler(console_hdlr)

def get_config(config_path):
    log.info ('Loading: %s' % config_path)
    config_fullpath = config_path
    if not path.exists(config_fullpath):
        log.error('I cannot find the config file %s.' % config_fullpath)
        exit(-1)

    try:
        config = __import__(path.splitext(path.basename(config_fullpath))[0])
        log.info('Config check passed...')
        return config
    except Exception:
        log.exception('I could not import your config from %s, please check the error below...' % config_fullpath)
        exit(-1)


class Config():
    def getConfig(self):
        raise NotImplementedError("getConfig function not defined")

class MyConfig(Config):
    def __init__(self, name):
        self.name = name

        a = MyConn('192.168.0.1',5000)
        b = MyVars()
        log.info (a)
        log.info (b)
        d = a.getConfig()
        v = b.getConfig()


        self.config_data =  { 'conn' : d,
                              'vars' : v,
                              'name' : self.name
                            }

    def getConfig(self):
        return self.config_data

class MyConn(Config):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __str__(self):
        return "IP: %s -- Port %s" % (self.ip, self.port)

    def getConfig(self):
        r = dict()
        r['ip'] = self.ip
        r['port'] = self.port
        return r

class MyVars(Config):
    def __init__(self):
        self.var1 = 'test1'
        self.var2 = ['test2','test3']

    def __str__(self):
        return "var1: %s\nvar2: %s" % (self.var1, self.var2)

    def getConfig(self):
        return [self.var1] + self.var2

if __name__ == '__main__':
    config = get_config('config.py')

    if hasattr(config, 'LOG_FORMATTER'):
        format_logs(formatter=config.BOT_LOG_FORMATTER)
    else:
        format_logs(theme_color=config.TEXT_COLOR_THEME)

    if config.LOG_FILE:
        hdlr = logging.FileHandler(config.LOG_FILE)
        hdlr.setFormatter(logging.Formatter("%(asctime)s %(levelname)-8s %(name)-25s %(message)s"))
        log.addHandler(hdlr)

    log.setLevel(config.LOG_LEVEL)
    log.info(config)
    i = MyConfig(config.SOME_NAME)
    j = json.dumps(i.getConfig(), sort_keys=True,indent=4)
    log.info(j)

