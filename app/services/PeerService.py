# File: application/services.py
import subprocess

from app.db import AppDb
from app.models import Peer
from app.repositories.InterfaceRepository import InterfaceRepository
from app.repositories.PeerRepository import PeerRepository


class PeerService:
    def __init__(self):
        db = AppDb()
        self.interface_repository = InterfaceRepository(db)
        self.repository = PeerRepository(db)

    def add_peer(self, name, description, interface, ipv4, ipv6, primary_dns, secondary_dns, nat):
        # Generate private and public keys
        private_key = subprocess.check_output(["wg", "genkey"]).strip()
        public_key = subprocess.check_output(["wg", "pubkey"], input=private_key, stdin=subprocess.PIPE).strip()

        # get interface public key
        interface_public_key = self.repository.getInterface(interface).public_key

        # Create peer with keys
        peer = Peer(name, description, interface, ipv4, ipv6, primary_dns, secondary_dns, public_key, private_key, nat)

        self.repository.addPeer(peer)

        # Update WireGuard configuration
        # ... existing logic ...

    # Similar methods for getting, updating, and deleting peers
