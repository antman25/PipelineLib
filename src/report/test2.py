#!/usr/bin/python3

import json

class Config():
    def getConfig(self):
        raise NotImplementedError("getConfig function not defined")

class MyConfig(Config):
    def __init__(self, name):
        self.name = name

        a = MyConn('192.168.0.1',5000)
        b = MyVars()
        print (a)
        print (b)
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


c = MyConfig('ant')

j= json.dumps(c.getConfig(), sort_keys=True,indent=4)
print(j)
#'{"a": 1, "b": 2}'
