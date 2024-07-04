import pytest
from modules.common.database import Database


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
    expected_order = (1, 'Sergii', 'солодка вода', 'з цукром')
    assert orders[0][:4] == expected_order