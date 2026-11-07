users = ["Emma", "Sam", "Alex", "Jordan"]
isAdmin = [True, False, True, False]

admins = [user for user, flag in zip(users, isAdmin) if flag]
print(admins)

scores = [72, 45, 88, 59, 91]
passed = [score for score in scores if score >= 60]
print(passed)

prices = [12, 45, 8, 30]
sale = [price * 0.9 for price in prices if price > 20]
print(sale)

my_score = 45
result = "pass" if my_score >= 60 else "fail"
print(result)
