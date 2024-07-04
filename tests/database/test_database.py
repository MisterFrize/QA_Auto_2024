import pytest
from modules.common.database import Database
import sqlite3

@pytest.mark.database
def test_database_connection():
    db = Database()
    version = db.test_connection()
    assert version is not None

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()
    print(users)
    assert users is not None

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    address = db.get_user_address_by_name('Sergii')
    expected_address = ('Maydan Nezalezhnosti 1', 'Kyiv', '3127', 'Ukraine')
    assert address == expected_address

@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    qnt = db.select_product_qnt_by_id(1)
    assert qnt[0] == 25

@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    qnt = db.select_product_qnt_by_id(4)
    assert qnt[0] == 30

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)
    assert qnt is None

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print(orders)
    assert len(orders) == 1
    expected_order = (1, 'Sergii', 'product_1', 'description')
    assert orders[0][:4] == expected_order
    
 #Individual part

@pytest.mark.database
def test_insert_invalid_data_type():
    db = Database()
    with pytest.raises(sqlite3.IntegrityError):
        db.insert_product('invalid_id', 'ім\'я', 'опис', 'wrong_qnt')

@pytest.mark.database
def test_insert_null_values():
    db = Database()
    db.connection.execute('BEGIN TRANSACTION')
    db.insert_product(10, None, None, None)
    db.connection.commit()
    product = db.select_product_qnt_by_id(10)
    assert product[0] is None

@pytest.mark.database
def test_unique_key_constraint():
    db = Database()
    db.insert_product(11, 'унікальний продукт', 'опис', 10)
    with pytest.raises(sqlite3.IntegrityError):
        db.insert_product(11, 'інший продукт', 'інший опис', 20)

@pytest.mark.database
def test_performance_large_data_set():
    db = Database()
    for i in range(1000):
        db.insert_product(i + 1000, f'product_{i}', 'description', i)
        db.connection.commit()
    
    products = db.get_all_users()
    assert len(products) >= 1000

@pytest.mark.database
def test_transaction_commit():
    db = Database()
    db.connection.execute('BEGIN TRANSACTION')
    db.insert_product(20, 'продукт транзакції', 'опис', 50)
    db.connection.commit()
    product = db.select_product_qnt_by_id(20)
    assert product[0] == 50

@pytest.mark.database
def test_transaction_rollback():
    db = Database()
    db.connection.execute('BEGIN TRANSACTION')
    db.insert_product(21, 'продукт транзакції', 'опис', 60)
    db.connection.rollback()
    product = db.select_product_qnt_by_id(21)
    assert product is None