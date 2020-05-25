import os

class Utils:
    @staticmethod
    def ping(hostname):
        return os.system("ping -c 1 -w 2 " + hostname) == 0

    @staticmethod
    def uptime():
        return os.popen("uptime").read()