class InterfaceRepository:
    def __init__(self, db):
        self.db = db

    def save(self, interface) -> int:
        cursor = self.db.cursor()
        cursor.execute(
            'INSERT INTO interfaces (name, description, gateway, address, listen_port, on_up, on_down) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (interface.name, interface.description, interface.gateway, interface.address, interface.listen_port,
             interface.on_up, interface.on_down))
        self.db.commit()
        cursor.close()
        return cursor.lastrowid

    def update(self, interface):
        cursor = self.db.cursor()
        cursor.execute(
            'UPDATE interfaces SET name=?, description=?, gateway=?, address=?, listen_port=?, on_up=?, on_down=? WHERE id=?',
            (interface.name, interface.description, interface.gateway, interface.address, interface.listen_port,
             interface.on_up, interface.on_down, interface.id))
        self.db.commit()
        cursor.close()

    def delete(self, interface):
        cursor = self.db.cursor()
        cursor.execute('DELETE FROM interfaces WHERE id=?', (interface.id,))
        self.db.commit()
        cursor.close()

    def get(self, id):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM interfaces WHERE id=?', (id,))
        row = cursor.fetchone()
        cursor.close()
        return row

    def getByName(self, name):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM interfaces WHERE name=?', (name,))
        row = cursor.fetchone()
        cursor.close()
        return row

    def getAll(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM interfaces')
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def getList(self, limit, offset):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM interfaces LIMIT ? OFFSET ?', (limit, offset))
        rows = cursor.fetchall()
        cursor.close()
        return rows

    # limit, offset, search:optional,sort:optional, order:optional
    def getListByFilter(self, limit, offset, search, sort, order):
        cursor = self.db.cursor()
        if search is None:
            search = ''
        if sort is None:
            sort = 'id'
        if order is None:
            order = 'asc'
        cursor.execute('SELECT * FROM interfaces WHERE name LIKE ? ORDER BY ? ? LIMIT ? OFFSET ?',
                       ('%' + search + '%', sort, order, limit, offset))
        rows = cursor.fetchall()
        cursor.close()
        return rows
