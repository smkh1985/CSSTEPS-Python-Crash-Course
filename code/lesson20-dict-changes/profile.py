profile = {}
print(profile)

profile["name"] = "Emma"
profile["age"] = 19
print(profile)

profile["age"] = 20
print(profile)

profile["name"] = "Emma Clark"
print(profile)

del profile["age"]
print(profile)

profile.update({"major": "Physics", "year": 2})
print(profile)
