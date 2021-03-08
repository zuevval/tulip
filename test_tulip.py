from tulip import first_sunday, commit_on


def test_first_monday():
    m = first_sunday(1999)
    assert m.weekday() == 6

    m = first_sunday(2021)
    assert m.month == 1
    assert m.day == 3


def test_commit_on():
    assert commit_on(date=first_sunday(2019)) == 0
