print("This program can calculate numbers")


while(True):
    print("type in operation (addition = a, subtraction = s, division = d, multiplcation = m, quit = q")
    operation = input()
    
    if operation == "q":
        break

    c = float(input("Type in a number"))
    b = float(input("Type in another number"))

    if operation == "a":
        answer = c + b
        print(answer)
    if operation == "s":
        answer = c - b
        print(answer)
    if operation == "d":
        answer = c/b
        print(answer) 
    if operation == "m":
        answer = c * b
        print(answer)
