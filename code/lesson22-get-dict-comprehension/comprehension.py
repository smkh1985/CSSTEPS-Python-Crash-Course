squares = {n: n * n for n in range(1, 6)}
print(squares)

names = ["Emma", "Sam", "Olivia"]
lengths = {name: len(name) for name in names}
print(lengths)

scores = {"Emma": 92, "Sam": 54, "Olivia": 85, "Liam": 58}
passed = {name: score for name, score in scores.items() if score >= 60}
print(passed)
