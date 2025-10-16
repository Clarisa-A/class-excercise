from app import add

def test_add_negative():
    assert add(-2, 3) == 1
