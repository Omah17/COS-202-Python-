print("=" * 45)
print("      MATHEMATICAL CALCULATOR (MC)")
print("=" * 45)

while True:

    print("\nChoose an Operation")
    print("+   Addition")
    print("-   Subtraction")
    print("*   Multiplication")
    print("/   Division")
    print("\\   Floor Division")
    print("^   Power")
    print("%   Modulus")
    print("C   Clear Screen")
    print("OFF Exit Calculator")

    operation = input("\nEnter your choice: ").upper()

    match operation:

        case "OFF":
            print("\nCalculator Closed.")
            break

        case "C":
            print("\nScreen Cleared.")

        case "+" | "-" | "*" | "/" | "\\" | "^" | "%":

            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))

            match operation:

                case "+":
                    print("Answer =", first_number + second_number)

                case "-":
                    print("Answer =", first_number - second_number)

                case "*":
                    print("Answer =", first_number * second_number)

                case "/":
                    if second_number == 0:
                        print("Error! Division by zero is not allowed.")
                    else:
                        print("Answer =", first_number / second_number)

                case "\\":
                    if second_number == 0:
                        print("Error! Division by zero is not allowed.")
                    else:
                        print("Answer =", first_number // second_number)

                case "^":
                    print("Answer =", first_number ** second_number)

                case "%":
                    if second_number == 0:
                        print("Error! Division by zero is not allowed.")
                    else:
                        print("Answer =", first_number % second_number)

        case _:
            print("Invalid Operation! Please try again.")