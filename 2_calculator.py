def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y != 0:
        return x / y


def main():
    print("Welcome to the simple calculator")
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))

    print("Choose an operation:")
    print(1, "1.Add")
    print(2, "2.Substract")
    print(3, "3.Multiply")
    print(4, "4.Divide")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = sub(num1, num2)
    elif choice == 3:
        result = mul(num1, num2)
    elif choice == 4:
        result = div(num1, num2)

    else:
        result = "Individual choice.Please select a valid operation."

    print(f"Result:{result}")


if __name__ == "__main__":
    main()
