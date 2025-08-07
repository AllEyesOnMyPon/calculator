# ===================================================================================

history = []  # list to store operation history
import math  # import math module
action_sequence_A = ["+", "-", "*", "/", "**"]  # operation symbols for: [number, action, number]
action_sequence_B = ["root", "log"]  # operation symbols for: [action, number, number]
action_sequence_C = ["sin", "cos", "tan", "cot"]  # operation symbols for: [action, number]

# Define the welcome function
def welcome():
    return (
        "--------------------------------------------------------------------------------------------------------\n"
        "--------------------------------------------------------------------------------------------------------\n"
        "                                                                                                        \n"
        "                                                                           Welcome to My calculator v2.0\n"
    )

# Define the instructions function
def help():
    return (
        "--------------------------------------------------------------------------------------------------------\n"
        "This is the instructions for using the calculator.\n"
        "--------------------------------------------------------------------------------------------------------\n"
        "--------------------------------------------------------------------------------------------------------\n"
        "ADD        | ACTION:   +       | STYLE:    1 + 1       | METHOD:    num_1[spacebar]action[spacebar]num_2\n"
        "SUBTRACT   | ACTION:   -       | STYLE:    1 - 1       | METHOD:    num_1[spacebar]action[spacebar]num_2\n"
        "MULTIPLY   | ACTION:   *       | STYLE:    1 * 1       | METHOD:    num_1[spacebar]action[spacebar]num_2\n"
        "DIVIDE     | ACTION:   /       | STYLE:    1 / 1       | METHOD:    num_1[spacebar]action[spacebar]num_2\n"
        "POWER      | ACTION:   **      | STYLE:    1 ** 1      | METHOD:    num_1[spacebar]action[spacebar]num_2\n"
        "ROOT       | ACTION:   root    | STYLE:    root 1 1    | METHOD:    action[spacebar]num_1[spacebar]num_2\n"
        "LOG        | ACTION:   log     | STYLE:    log 1 1     | METHOD:    action[spacebar]num_1[spacebar]num_2\n"
        "SINUS      | ACTION:   sin     | STYLE:    sin 1       | METHOD:    action[spacebar]num_1\n"
        "COSINUS    | ACTION:   cos     | STYLE:    cos 1       | METHOD:    action[spacebar]num_1\n"
        "TANGENS    | ACTION:   tan     | STYLE:    tan 1       | METHOD:    action[spacebar]num_1\n"
        "COTANGENS  | ACTION:   cot     | STYLE:    cot 1       | METHOD:    action[spacebar]num_1\n"
        "--------------------------------------------------------------------------------------------------------\n"
        "Please enter the task in the correct format as shown above.\n"
        "--------------------------------------------------------------------------------------------------------\n"
        "--------------------------------------------------------------------------------------------------------\n"
    )

# Define the short menu function
def short_menu():
    return (
        "--------------------------------------------------------------------------------------------------------\n"
        "NEW CALC:  Press 1              |               MENU:   Press 2            |             EXIT:   Press 3\n"
        "--------------------------------------------------------------------------------------------------------\n"
    )

# Define the long menu function
def long_menu():
    return (
        "--------------------------------------------------------------------------------------------------------\n"
        "This is the menu for using the calculator.\n"
        "--------------------------------------------------------------------------------------------------------\n"
        "New calculation:   Press 1\n"
        "Show history:      Press 2\n"
        "Help:              Press 3\n"
        "Exit:              Press 4\n"
        "--------------------------------------------------------------------------------------------------------\n"
    )

# ===================================================================================

def add(number_1, number_2):  # addition function
    return number_1 + number_2  # return sum result

def subtract(number_1, number_2):
    return number_1 - number_2  # return subtraction result

def multiply(number_1, number_2):
    return number_1 * number_2  # return multiplication result

def divide(number_1, number_2):
    try:
        if number_2 == 0:
            raise ZeroDivisionError
        return number_1 / number_2
    except ZeroDivisionError:
        print("You can't divide by 0!")
        return None

def power(number_1, number_2):
    return number_1 ** number_2  # return exponentiation result

def root(number_1, number_2):
    if number_2 == 0:  # check if root degree is 0 (undefined)
        return "Root degree cannot be 0"
    elif number_1 < 0 and number_2 % 2 == 0:  # negative number with even root
        return "Invalid root operation for negative numbers with even roots"
    return number_1 ** (1 / number_2)  # return root result

def log(number_1, number_2):
    if number_1 <= 0 or number_2 <= 0 or number_2 == 1:  # check for valid input
        return "Invalid log operation"
    return math.log(number_1, number_2)  # return logarithm result

def sin(number_1):
    return math.sin(number_1)  # return sine result

def cos(number_1):
    return math.cos(number_1)  # return cosine result

def tan(number_1):
    try:
        # check if angle is near 90° (π/2) or 270° (3π/2)
        if number_1 % math.pi == math.pi / 2 or number_1 % math.pi == 3 * math.pi / 2:
            return "Undefined"
        return math.tan(number_1)  # return tangent result
    except ZeroDivisionError:
        return "Undefined"

def cot(number_1):
    try:
        if math.cos(number_1) == 0:  # check if cosine equals 0
            return "Undefined"
        return 1 / math.tan(number_1)  # return cotangent result
    except ZeroDivisionError:
        return "Undefined"

# ===================== WELCOME SECTION =====================================================

welcome_info = welcome()
print(welcome_info)

help_info = help()
print(help_info)

# ===================== MAIN PROGRAM LOOP ===================================================

while True:
    user_task = input("Write math calculation: ")
    user_task_list = user_task.split()

    # Check which type of operation
    if any(op in user_task_list for op in action_sequence_A):
        # Operations with two numbers
        try:
            number_1, action, number_2 = user_task_list
            number_2 = float(number_2)
        except ValueError:
            print("Invalid number! Please enter valid numbers.")
            continue

    elif any(op in user_task_list for op in action_sequence_B):
        # Operations with two numbers (root, log)
        try:
            action, number_1, number_2 = user_task_list
            number_1, number_2 = float(number_1), float(number_2)
        except ValueError:
            print("Invalid number! Please enter valid numbers.")
            continue

    elif any(op in user_task_list for op in action_sequence_C):
        # Operations with one number (sin, cos, tan, cot)
        try:
            action, number_1 = user_task_list
            number_1 = float(number_1)
            number_2 = None
        except ValueError:
            print("Invalid number! Please enter valid numbers.")
            continue

    else:
        print("Invalid input! Please enter a valid task (e.g. 2 + 2, root 4 2, sin 30, etc.).")
        continue

    number_1 = float(number_1)
    if number_2 is not None:
        number_2 = float(number_2)
    else:
        number_2 = None

# ===================== PERFORM CALCULATIONS ================================================

    if action in action_sequence_A:
        if action == "+":
            result = add(number_1, number_2)
        elif action == "-":
            result = subtract(number_1, number_2)
        elif action == "*":
            result = multiply(number_1, number_2)
        elif action == "/":
            result = divide(number_1, number_2)
        elif action == "**":
            result = power(number_1, number_2)

    elif action in action_sequence_B:
        if action == "root":
            result = root(number_1, number_2)
        elif action == "log":
            result = log(number_1, number_2)

    elif action in action_sequence_C:
        if action == "sin":
            result = sin(number_1)
        elif action == "cos":
            result = cos(number_1)
        elif action == "tan":
            result = tan(number_1)
        elif action == "cot":
            result = cot(number_1)

# ===================== HISTORY HANDLING =====================================================

    if result is not None:
        if action in action_sequence_A:
            print(f"{number_1} {action} {number_2} = {result}")
        elif action in action_sequence_B:
            print(f"{action} {number_1} {number_2} = {result}")
        elif action in action_sequence_C:
            print(f"{action} {number_1} = {result}")

        print("--------------------------------------")
        print("Operation added to history.")
        history.append((number_1, action, number_2, result))

    # Short menu loop
    while True:
        show_short_menu = short_menu()
        print(show_short_menu)
        user_choice_short_menu = input("Choose the path: ")
        if user_choice_short_menu not in ["1", "2", "3"]:
            print("Invalid input! Please enter demanded path.")
            continue
        elif user_choice_short_menu == "1":
            break
        elif user_choice_short_menu == "2":
            show_long_menu = long_menu()
            print(show_long_menu)
            user_choice_long_menu = input("Choose the path: ")
            if user_choice_long_menu == "4":
                print("Thank you for using the program!")
                input("Press Enter to exit...")
                break
            elif user_choice_long_menu == "3":
                print(help_info)
                continue
            elif user_choice_long_menu == "2":
                print("Calculation History:")
                for record in history:
                    print(f"{record[0]} {record[1]} {record[2]} = {record[3]}")
                continue
            elif user_choice_long_menu == "1":
                break
        elif user_choice_short_menu == "3":
            print("Thank you for using the program!")
            input("Press Enter to exit...")
            break

# ===================== END OF PROGRAM =======================================================
