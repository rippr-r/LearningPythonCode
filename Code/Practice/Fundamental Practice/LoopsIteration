def left_triangle_maker():
    for i in range(1, 6):
        print("*" * i)

def right_triangle_maker():
    for i in range(1, 6):
        print(("*" * i).rjust(5)) # Right align the stars within a width of 5

def centered_triangle_maker():
    height = 5
    for i in range(1, height + 1):
        stars = '*' * (2*i - 1)
        print(stars.center(2*height - 1)) # Center align the stars within a width of 2*height - 1

def triangles():
    left_triangle_maker()
    print()  # Print a blank line between triangles
    right_triangle_maker()
    print()  # Print a blank line between triangles
    centered_triangle_maker()

def main():
    triangles()

main()
