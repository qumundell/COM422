
def get_ticket_price(age, student=False):
    if age >= 65 or age < 3:
        return 0
    elif age < 19 and student is True:
        return 2
    else:
        return 4
