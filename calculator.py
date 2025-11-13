def calculator():
    print("CALCULATOR!")

    def add(num1, num2):
        return num1+num2

    def subtract(num1, num2):
        return num1-num2

    def multiply(num1, num2):
        return num1*num2

    def divide(num1, num2):
        if num2 ==0:
            return "Zero division error"
        return num1/num2

    calculate= True

    while calculate:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue
        operator= input("Enter the operator: ")

        if operator == "+":
            print("Result: ", add(num1, num2))
        elif operator == "-":
            print("Result: ", subtract(num1, num2))
        elif operator == "*":
            print("Result: ", multiply(num1, num2))
        elif operator == "/":
            print("Result: ", divide(num1, num2))
        
        again= input("Do you want to calculate again (yes/no): ")
        if again!= "yes":
            print("END!")
            calculate= False

calculator()