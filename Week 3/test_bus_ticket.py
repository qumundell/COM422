import bus_ticket


def test_age_over_65():
    assert bus_ticket.get_ticket_price(70) == 0


def test_age_under_3():
    assert bus_ticket.get_ticket_price(2) == 0


def test_student_under_19():
    assert bus_ticket.get_ticket_price(18, True) == 2


def test_student_over_18():
    assert bus_ticket.get_ticket_price(30, True) == 4


def test_age_over_18():
    assert bus_ticket.get_ticket_price(30) == 4
