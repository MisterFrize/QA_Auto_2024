import pytest


class User:
    def __init__(self, name=None, second_name=None):
        self.name = name
        self.second_name = second_name

    def create(self):
        self.name = "Dmytro"
        self.second_name = "Maltsev"

    def remove(self):
        self.name = ""
        self.second_name = ""

@pytest.fixture
def user():
    user_instance = User()
    user_instance.create()
    yield user_instance
    user_instance.remove()