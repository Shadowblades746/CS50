from twttr import shorten


def test_random():
    assert shorten("rythm") == "rythm"


def test_lowercase():
    assert shorten("aeiou") == ""


def test_uppercase():
    assert shorten("AEIOU") == ""


def test_numbers():
    assert shorten("123") == "123"


def test_punctuation():
    assert shorten(",./") == ",./"
