from bank import value


def test_hello():
    assert value("hello") == 0


def test_begining_with_h():
    assert value("Hi") == 20


def test_random():
    assert value("wys g") == 100
