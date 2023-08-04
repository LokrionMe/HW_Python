import pytest
from Project import Project
from task4 import User
from Exceptions import AccessError

@pytest.fixture
def data():
    return Project().read_users('users')

def test_data(data: Project):
    assert len(data.list_users) == 3

def test_add(data: Project):
    a = User('vitalya', 1, 1)
    assert data.add_user(a) == "Please login before to try to add users"

def test_login(data: Project):
    assert data.login('vitalya', 1) == "Welcome, vitalya"

def test_add_admin(data: Project):
    a = User('pasha', 6, 3)
    data.login('vitalya', 1)
    data.add_user(a)
    assert len(data.list_users) == 4

def test_delete_user(data: Project):
    a = User('pasha', 6, 3)
    data.login('vitalya', 1)
    with pytest.raises(AccessError):
        assert data.delete_user(a)
