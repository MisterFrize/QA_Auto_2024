import sqlite3


class Database:
    def __init__(self, db_name=':memory:'):
        self.connection = sqlite3.connect(r'C:\\Users\\andro\\QA_Auto_2024' + r'\\become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        self.cursor.execute('SELECT sqlite_version();')
        version = self.cursor.fetchone()
        print(version)
        return version

    def get_all_users(self):
        self.cursor.execute('SELECT name, address, city FROM customers')
        return self.cursor.fetchall()

    def get_user_address_by_name(self, name):
        self.cursor.execute('''
            SELECT address, city, postalCode, country 
            FROM customers 
            WHERE name = ?
        ''', (name,))
        return self.cursor.fetchone()

    def update_product_qnt_by_id(self, product_id, qnt):
        self.cursor.execute('''
            UPDATE products 
            SET quantity = ? 
            WHERE id = ?
        ''', (qnt, product_id))
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        self.cursor.execute('SELECT quantity FROM products WHERE id = ?', (product_id,))
        return self.cursor.fetchone()

    def insert_product(self, product_id, name, description, qnt):
        self.cursor.execute('''
            INSERT OR REPLACE INTO products (id, name, description, quantity) 
            VALUES (?, ?, ?, ?)
        ''', (product_id, name, description, qnt))
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        self.cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
        self.connection.commit()

    def get_detailed_orders(self):
        self.cursor.execute('''
            SELECT orders.id, customers.name, products.name, products.description 
            FROM orders 
            JOIN customers ON orders.customer_id = customers.id 
            JOIN products ON orders.product_id = products.id
        ''')
        return self.cursor.fetchall()