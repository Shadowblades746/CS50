from numb3rs import validate

def test_validate():
    assert validate("1.1.1.1") == True
    assert validate("dog") == False
    assert validate("1.1.1.256") == False
    assert validate("256.256.256.256") == False