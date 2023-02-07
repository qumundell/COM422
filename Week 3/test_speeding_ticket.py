import speeding_ticket


def test_speeding_over_10mph():
    assert speeding_ticket.speeding_fine(45) == (True, True)


def test_speeding_under_10mph():
    assert speeding_ticket.speeding_fine(35) == (True, False)


def test_not_speeding():
    assert speeding_ticket.speeding_fine(30) == (False, False)
