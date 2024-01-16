import socket

class ServerInfo:
    """
    This class saves information about a remote host
    """
    def __init__(self, config):
        self._hostname = config['hostname']
        self.login = config['username']
        self.password = config['password']
        self._ip = None

    @property
    def hostname(self):
        return self._hostname

    @hostname.setter
    def hostname(self, new_value):
        self._ip = None
        self._hostname = new_value


    @property
    def ip(self):
        if self._ip is None:
            self._ip = socket.gethostbyname(self.hostname)
        return self._ip






config = {"hostname": "journaldev.com", "username": "admin", "password": "admin"}
info = ServerInfo(config)
print(info.login)

for i in range(100):
    print(info.ip)

info.hostname = 'ynonperek.com'
print(info.ip)
