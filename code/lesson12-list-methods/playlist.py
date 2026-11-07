playlist = ["Waves", "Sunrise", "Echo", "Sunrise"]

print(len(playlist))
print("Echo" in playlist)
print(playlist.count("Sunrise"))
print(playlist.index("Echo"))

playlist.extend(["Comet", "Breeze"])
print(sorted(playlist))
print(playlist)
