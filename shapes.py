print("enter 1 to calclate circle area/perimeter")
print("enter 2 to calclate square  area/perimeter")
print("enter 3 to calclate rectangle  area/perimeter")


i = 0
while i<10:
    option = int(input())
    i = i+1
    print(i)
    if option == 1: 
        radius = float(input())
        pi = 3.147

        area = pi * radius * radius
        circumference = 2 * pi * radius
        print(area, "is the area of the circle")
        print(circumference, "is the circumference of the circle")
    elif option == 2:
        l = int(input())

        area = l * l 
        perimeter = 4 * l 
        print(area, "is the area of the square")
        print(perimeter, "is the perimeter of the square")
    elif option == 3:
        l = int(input())
        w = int(input())

        area = l * w
        perimeter = (2 * l) + (2 * w)
        print(area, "is the area of the square")
        print(perimeter,"is the perimeter of the square" ) 

