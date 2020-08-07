
class MyConn():
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
