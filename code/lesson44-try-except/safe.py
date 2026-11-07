f = open("notes.txt", "w")
try:
    f.write("Hello, file!")
    number = int("abc")
finally:
    f.close()
    print("File closed")
