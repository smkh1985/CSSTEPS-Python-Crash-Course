from grades import average, letter


def test_average():
    assert average([90, 80, 70]) == 80


def test_average_empty():
    assert average([]) == 0


def test_letter_edges():
    assert letter(90) == "A"
    assert letter(89.9) == "B"
    assert letter(0) == "F"


def test_letter_of_average():
    assert letter(average([95, 85, 72])) == "B"
