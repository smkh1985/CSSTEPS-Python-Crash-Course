import random


def spin():
    prizes = ["No prize", "Small prize", "Big prize", "Jackpot"]
    shares = [70, 20, 9, 1]
    return random.choices(prizes, weights=shares)[0]
