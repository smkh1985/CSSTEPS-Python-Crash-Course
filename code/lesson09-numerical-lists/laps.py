distances = []

for lap in range(1, 5):
    distances.append(lap * 400)
    
print(distances)

distances = [lap * 400 for lap in range(1, 5)]
print(distances)
