import day2.object_oriented_day9 as day9

def test_tail_follows_head():
    h = day9.Head()
    t = day9.Tail(h)
    h.position = day9.Position(x=2, y=2)

    t.follow()
    assert t.position == day9.Position(x=1, y=1)


def test_tail_follows_head_2():
    h = day9.Head()
    t = day9.Tail(h)
    h.position = day9.Position(x=0, y=0)

    t.follow()
    assert t.position == day9.Position(x=0, y=0)


def test_tail_follows_head_3():
    h = day9.Head()
    t = day9.Tail(h)
    h.position = day9.Position(x=-2, y=0)

    t.follow()
    assert t.position == day9.Position(x=-1, y=0)


def test_tail_follows_head_4():
    h = day9.Head()
    t = day9.Tail(h)
    h.position = day9.Position(x=4, y=-2)
    t.position = day9.Position(x=3, y=0)

    t.follow()
    assert t.position == day9.Position(x=4, y=-1)
