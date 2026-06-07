import math

def area_circle():
    radius = float(input("Enter radius: "))
    area = math.pi * radius * radius
    print("Area of Circle =", area)

def area_rectangle():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    print("Area of Rectangle =", area)

def area_triangle():
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area of Triangle =", area)

while True:

    print("\nMenu Options:")
    print("1. Area of Circle")
    print("2. Area of Rectangle")
    print("3. Area of Triangle")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        area_circle()

    elif choice == "2":
        area_rectangle()

    elif choice == "3":
        area_triangle()

    elif choice == "4":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")