import wheel

counts = {}
for i in range(1000):
    prize = wheel.spin()
    counts[prize] = counts.get(prize, 0) + 1
print(counts)
