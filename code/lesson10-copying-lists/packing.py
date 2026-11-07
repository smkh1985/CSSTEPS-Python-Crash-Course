l1 = ["tent", "flashlight", "water bottle"]
l2 = l1[:]

l2[1] = "headlamp"
print("List 2:", l2)
print("List 1:", l1)

l1[0] = "hammock"
print("List 1 after the second edit:", l1)
print("List 2 after the second edit:", l2)

print("List 1 ID:", id(l1))
print("List 2 ID:", id(l2))
