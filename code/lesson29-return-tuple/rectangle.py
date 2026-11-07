def rectangle(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter
    
area, perimeter = rectangle(5, 3)
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
