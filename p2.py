while True:
    print("\nPlease select operation -\n" \
          "1. Add\n" \
          "2. Subtract\n" \
          "3. Multiply\n" \
          "4. Divide\n"
          "5. Div\n"
          "6. Dis\n")
    
    operator = int(input("Select operations from 1, 2, 3, 4, 5, 6: "))
    
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))
    
    if operator == 1:
        print(number_1, "+", number_2, "=", number_1 + number_2)
    
    elif operator == 2:
        print(number_1, "-", number_2, "=", number_1 - number_2)
    
    elif operator == 3:
        print(number_1, "*", number_2, "=", number_1 * number_2)
    
    elif operator == 4:
        print(number_1, "/", number_2, "=", number_1 / number_2)
    
    else:
        print("Invalid input")
