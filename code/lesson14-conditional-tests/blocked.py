blocked = ["spam", "scam"]
word = "scam"

print(word in blocked)
print("hello" in blocked)
print("hello" not in blocked)

for item in blocked:
    print(item)
