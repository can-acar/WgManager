class Interface:
    def __init__(self, name=None, description=None, gateway=None, ipv4=None, ipv6=None, listen_port=None, on_up=None,
                 on_down=None, private_key=None, public_key=None):
        self.name = name
        self.description = description
        self.gateway = gateway
        self.ipv4 = ipv4
        self.ipv6 = ipv6
        self.listen_port = listen_port
        self.on_up = on_up
        self.on_down = on_down
        self.private_key = private_key
        self.public_key = public_key
