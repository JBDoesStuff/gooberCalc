import time

def print_result(result):
    if result == 69:
        print()
        print(result)
        print("Nice.")
        print()
    elif result == 420:
        print()
        print(result)
        print("You must be a Coloradan, huh?")
        print()
    elif result == 69420:
        print()
        print("ERR 642: TOO MUCH COMEDY")
        print("MAYBE DON'T TRY TO BE FUNNY")
        time.sleep(5)
        quit()
    elif result == [8008, 80085, 58008, 5318008, 8008135]:
        print()
        print(result)
        print("You're a child, aren't you?")
        print()
    elif result == 0:
        print()
        print(result)
        print("Yeah, cool.")
        print()
    elif result >= 1000000000000000 or result <= -1000000000000000:
        print()
        print("ERR 999: INTERNAL OVERFLOW")
        print("TRY TO NOT CALCULATE THE NUMBER OF ATOMS IN THE UNIVERSE")
        time.sleep(5)
        quit()
    elif result >= 1000000000000 or result <= -1000000000000:
        print()
        print(result)
        print("You're just trying to break it now, aren't you?")
        print()
    elif result >= 1000000000 or result <= -1000000000:
        print()
        print(result)
        print("What are you even doing?")
        print("I didn't make this calculator to handle numbers that big.")
        print()
    elif isinstance(result, int) and result <= 20 and result >= -20 and (operation == "1" or operation == "2"):
        print()
        print("Count on your fingers. Whatever, here's your answer:")
        print()
        print(result)
        print()
    elif result == 42:
        print()
        print("ERR 042: MEANING OF LIFE")
        print("DON'T TRY TO CALCULATE THE MEANING OF LIFE")
        print()
    elif result == 29:
        print()
        print(result)
        print("NUMBER 29, NATHAN MACKINNON!")
        print()
    elif abs(result) <= 0.00000000000000000001 and result != 0:
        print(result)
        print("ERR 000: REALLY SMALL NUMBER")
        print("DON'T TRY TO DO QUANTUM MECHANICS WITH THIS CALCULATOR")
        time.sleep(5)
        quit()
    elif abs(result) <= 0.00000000001 and result != 0:
        print()
        print(result)
        print("That's a really small number.")
        print("I'm not even sure what to do with that.")
        print()
    else:
        print()
        print(result)
        print()

print("Hello!")
print("Welcome to my calculator!")

while True:
    print("Select your operation by number:")
    print("1 for addition.")
    print("2 for subtraction.")
    print("3 for multiplication.")
    print("4 for division.")
    print("5 for exponentiation.")
    print("6 for info.")
    print("7 to exit.")

    operation = input("Enter here: ")

    if operation == "1":
        print("Selected addition.")
        value1 = float(input("Enter first value here: "))
        value2 = float(input("Enter second value here: "))
        if value1 == 9 and value2 == 10:
            print()
            print("You stupid.")
            print("Nah I'm not.")
            print("What's 9 + 10?")
            print("21")
            print("You stupid.")
            print()
        elif value2 == 0:
            print()
            print("ERR 010: ADDING ZERO")
            print("WHY WOULD YOU DO THAT?")
            time.sleep(5)
            quit()
        result = value1 + value2
        print_result(result)
    elif operation == "2":
        print("Selected subtraction.")
        value1 = float(input("Enter first value here: "))
        value2 = float(input("Enter second value here: "))
        result = value1 - value2
        if value2 == 0:
            print()
            print("ERR 020: SUBTRACTING ZERO")
            print("WHY WOULD YOU DO THAT?")
            time.sleep(5)
            quit()
        print_result(result)
    elif operation == "3":
        print("Selected multiplication.")
        value1 = float(input("Enter first value here: "))
        value2 = float(input("Enter second value here: "))
        if value1 == 0 and value2 == 0:
            print()
            print("ERR 030: MULTIPLYING ZERO BY ZERO")
            print("JUST... WHY?")
            print()
        elif value1 == 0 or value2 == 0:
            print()
            print("0")
            print("You think that would be obvious.")
            print()
        else:
            result = value1 * value2
            print_result(result)
    elif operation == "4":
        print("Selected division.")
        value1 = float(input("Enter dividend here: "))
        value2 = float(input("Enter divisor here: "))
        if value1 == 0 and value2 == 0:
            print()
            print("ERR 000: ZERO DIVIDED BY ZERO")
            print("WOW, REAL CREATIVE")
            print()
            print("WAIT... IS THE ANSWER 1?")
            time.sleep(5)
            quit()
        elif value2 == 0:
            print()
            print("ERR 040: DIVISION BY ZERO")
            print("YOU CAN'T DIVIDE BY ZERO")
            print("DON'T YOU KNOW THAT?")
            time.sleep(5)
            quit()
        elif value1 == 0:
            print()
            print("0")
            print("Just think about it.")
            print()
        elif value1 == 22 and value2 == 7:
            print()
            print("π")
            print()
        else:
            result = value1 / value2
            print_result(result)
    elif operation == "5":
        print("Selected exponentiation.")
        value1 = float(input("Enter first value here: "))
        value2 = float(input("Enter second value here: "))
        result = value1 ** value2
        print_result(result)
    elif operation == "6":
        print()
        print("Made by JBDoesStuff.")
        print("What all are you asking for?")
        print()
    elif operation == "7":
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid operation selected. Please try again.")
