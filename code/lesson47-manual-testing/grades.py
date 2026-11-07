def average(grades):
    if not grades:
        return 0
    return f"{sum(grades) / len(grades):.1f}"


def letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
