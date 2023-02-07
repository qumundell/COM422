
def speeding_fine(speed):
    if speed > 30 + 10:
        return True, True
    elif speed <= 30:
        return False, False
    else:
        return True, False

