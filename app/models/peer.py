class Peer:
    def __init__(self, name=None,
                 description=None,
                 interface=None,
                 ipv4=None,
                 ipv6=None,
                 primary_dns=None,
                 secondary_dns=None,
                 public_key=None,
                 private_key=None,
                 nat=None):
        self.name = name
        self.description = description
        self.interface = interface
        self.ipv4 = ipv4
        self.ipv6 = ipv6
        self.primary_dns = primary_dns
        self.secondary_dns = secondary_dns
        self.public_key = public_key
        self.private_key = private_key
        self.nat = nat
