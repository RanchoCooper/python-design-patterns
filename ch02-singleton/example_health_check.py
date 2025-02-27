class HealthCheck:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance

    def __init__(self):
        self._servers = []

    def add_servers(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")

    def change_server(self):
        self._servers.pop()
        self._servers.append("Server 5")

    @property
    def servers(self):
        return self._servers


if __name__ == '__main__':
    hc1 = HealthCheck()
    hc2 = HealthCheck()

    hc1.add_servers()
    print("Schedule health check for servers (1)..")
    for i in range(4):
        print("Checking ", hc1.servers[i])

    hc2.change_server()
    print("Schedule health check for servers (2)..")
    for i in range(4):
        print("Checking ", hc2.servers[i])
    print("Schedule health check for servers (1) again..")
    for i in range(4):
        print("Checking ", hc1.servers[i])
