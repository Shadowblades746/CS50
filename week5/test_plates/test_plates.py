from plates import is_valid


def test_alpha():
    assert is_valid("alpha") == True


def test_valid():
    assert is_valid("CS50") == True


def test_zero():
    assert is_valid("cs05") == False


def test_embedded_number():
    assert is_valid("cs50p") == False


def test_punctuation():
    assert is_valid("PI3.14") == False


def test_lower_len():
    assert is_valid("H") == False


def test_uppper_len():
    assert is_valid("outatime") == False


def test_begining_number():
    assert is_valid("69") == False
