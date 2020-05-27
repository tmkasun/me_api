import os

SERVERS = {
    "dell": {
        "host": "plex.knnect.com",
        "mac": "18:66:da:35:4a:3a"
    },
    "jetson": {
        "host": "home.knnect.com",
    }
}


class Utils:
    @staticmethod
    def ping(hostname):
        return os.system("ping -c 1 -w 2 " + hostname) == 0

    @staticmethod
    def uptime(server='me'):
        if server == 'me':
            return os.popen("uptime").read()
        elif server == 'dell':
            return os.popen("ssh kasun@{} \"uptime\"".format(SERVERS[server]['host'])).read()

    @staticmethod
    def wakeOnLan(server='dell'):
        if server == 'dell':
            os.popen("sudo etherwake {}".format(SERVERS[server]['mac']))
            return True
        return False

    @staticmethod
    def powerOff(server='dell'):
        if server == 'dell':
            os.popen(
                "ssh -v kasun@{} \"sudo poweroff\"".format(SERVERS[server]['host']))
            return True
        elif server == 'me' or server == 'jetson':
            os.popen("sudo poweroff")
            return True
        return False
