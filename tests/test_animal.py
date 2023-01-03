import time
from domain.animal import Animal


def test_timer():
    a = Animal()

    start_health = a.health
    assert start_health >= 50

    time.sleep(5)

    assert abs(start_health - a.health) in range(4, 6)

def test_feed():
    assert


