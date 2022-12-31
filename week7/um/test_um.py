from um import count

def test_count():
    assert count("um") == 1
    assert count('cum') == 0
    assert count("hi um whats your UM name?") == 2