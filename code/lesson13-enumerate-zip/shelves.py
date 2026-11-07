books = ["Matilda", "Holes", "The Hobbit"]
shelves = ["A2", "B1", "C3"]

copies = [4, 2, 5]

for book, shelf, count in zip(books, shelves, copies):
    print(f"{book} | Shelf {shelf} | Copies {count}")
