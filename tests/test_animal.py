from domain.animal import Animal


def test_feed():
    a = Animal()
    print(a.health, a.hunger, a.mood, a.name)

    for _ in range(50):
        a.tick()

    print(a.health, a.hunger, a.mood, a.name)
    a.feed()
    a.play()
    a.wash()
    a.is_alive()
    print(a.health, a.hunger, a.mood, a.name)


