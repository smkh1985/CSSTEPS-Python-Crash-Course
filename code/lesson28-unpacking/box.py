def volume(length, width, height):
    print(f"Volume: {length * width * height}")

box = [2, 3, 4]
volume(*box)
print(*box)
