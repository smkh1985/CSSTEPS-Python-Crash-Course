data = dict(a=1, b=2, c=3)
print(data)

list_of_pairs = [("name", "Alice"), ("age", 25)]
profile = dict(list_of_pairs)
print(profile)

keys = ["id", "role"]
values = [101, "admin"]
session = dict(zip(keys, values))
print(session)
