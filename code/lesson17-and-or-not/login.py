usernames = ["alex", "alex", "sam"]
passwords = ["learn123", "1234", "learn123"]

for username, password in zip(usernames, passwords):
    if username == "alex" and password == "learn123":
        print(f"{username}: You logged in successfully.")
    else:
        print(f"{username}: The username or password is incorrect.")
