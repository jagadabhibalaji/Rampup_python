import math
arguments=[]
try:
    number_of_arguments=int(input("enter value for number of  arguments to pass and \n value should less than 4 : "))

    if number_of_arguments==2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        arguments.append(length)
        arguments.append(width)
    elif number_of_arguments==1:
        radius = float(input("Enter the radius of the circle: "))
        arguments.append(radius)
    elif number_of_arguments==3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        shape=input("enter 'triangle' word for the shape declaration").lower()
        arguments.append(base)
        arguments.append(height)
        arguments.append(shape)
    else:
        print("please give input according to requirement")

    if len(arguments)==2:
        def calculate_area(*args):
                return args[0][0] * args[0][1]

    elif len(arguments)==1:
        def calculate_area(*args):
            return math.pi * args[0][0]

    elif len(arguments)==3 and 'triangle' in arguments:
        def calculate_area(*args):
            return f"the triangle area is {args[0][0] * args[0][1]}"

    print(f"Area{calculate_area(arguments)}")
except:
    print("please ensure about given input argument")




#
# def calculate_rectangle_area():
#     length = float(input("Enter the length of the rectangle: "))
#     width = float(input("Enter the width of the rectangle: "))
#     return length * width
#
# def calculate_circle_area():
#     radius = float(input("Enter the radius of the circle: "))
#     return math.pi * radius ** 2
#
# def calculate_triangle_area():
#     base = float(input("Enter the base of the triangle: "))
#     height = float(input("Enter the height of the triangle: "))
#     return 0.5 * base * height
#
# while True:
#     print("Choose a shape to calculate area:")
#     print("1. Rectangle")
#     print("2. Circle")
#     print("3. Triangle")
#     print("4. Quit")
#
#     choice = input("Enter your choice (1/2/3/4): ")
#
#     if choice == '1':
#         area = calculate_rectangle_area()
#         print("The area of the rectangle is:", area)
#     elif choice == '2':
#         area = calculate_circle_area()
#         print("The area of the circle is:", area)
#     elif choice == '3':
#         area = calculate_triangle_area()
#         print("The area of the triangle is:", area)
#     elif choice == '4':
#         break
#     else:
#         print("Invalid choice. Please enter 1, 2, 3, or 4.")
