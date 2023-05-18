class PeerRepository:
    def __init__(self, db):
        self.db = db

    def addPeer(self, peer):
        cursor = self.db.cursor()
        cursor.execute(
            'INSERT INTO peers (name, description, interface, ipv4, ipv6, primary_dns, secondary_dns, public_key, private_key, nat) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (peer.name, peer.description, peer.interface, peer.ipv4, peer.ipv6, peer.primary_dns, peer.secondary_dns,
             peer.public_key, peer.private_key, peer.nat))
        self.db.commit()
        cursor.close()

    def updatePeer(self, peer):
        cursor = self.db.cursor()
        cursor.execute(
            'UPDATE peers SET name=?, description=?, interface=?, ipv4=?, ipv6=?, primary_dns=?, secondary_dns=?, public_key=?, private_key=?, nat=? WHERE id=?',
            (peer.name, peer.description, peer.interface, peer.ipv4, peer.ipv6, peer.primary_dns, peer.secondary_dns,
             peer.public_key, peer.private_key, peer.nat, peer.id))
        self.db.commit()
        cursor.close()

    def deletePeer(self, peer):
        cursor = self.db.cursor()
        cursor.execute('DELETE FROM peers WHERE id=?', (peer.id,))
        self.db.commit()
        cursor.close()

    def getPeer(self, id):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM peers WHERE id=?', (id,))
        row = cursor.fetchone()
        cursor.close()
        return row

    def getAllPeers(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM peers')
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def getPeerOfInterface(self, interface, page, limit=25, search=None, sort=None, order=None):
        cursor = self.db.cursor()
        if search is None:
            search = ''
        if sort is None:
            sort = 'name'
        if order is None:
            order = 'asc'
        cursor.execute(
            'SELECT * FROM peers WHERE interface=? AND name LIKE ? ORDER BY ? ? LIMIT ? OFFSET ?',
            (interface, '%' + search + '%', sort, order, limit, page * limit))
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def getInterface(self, interface):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM peers WHERE interface=?', (interface,))
        # Single row
        row = cursor.fetchone()
        cursor.close()
        return row
