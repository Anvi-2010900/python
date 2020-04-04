def add(c, b):
    answer = c + b
    return answer
def subtraction(c, b):
    answer = c - b
    return answer
def multiplcation(c, b):
    answer = c * b
    return answer
def division(c, b):
    answer = c/b
    return answer


def calculator():
    print("This program can calculate numbers")

    while(True):
        print("type in operation (addition = a, subtraction = s, division = d, multiplcation = m, quit = q")
        operation = input()
    
        if operation == "q":
            break

        #get input from user for c & b
        print("Enter 1st number")
        x = int(input())

        print("Enter 2nd number")
        y = int(input())

        if operation == "a":   
            sume = add(x, y)
            print("Addition of two numbers:" + str(sume))
        if operation == "s":
            difference = subtraction(x, y)
            print("subtraction of two numbers:" + str(difference))
        if operation == "d":
            quotient = division(x, y)
            print("division of two numbers:" + str(quotient))
        if operation == "m":
            product = multiplcation(x, y)
            print("multiplcation of two numbers:" + str(product))
