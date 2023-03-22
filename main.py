def encode(password):
    password = password
    encoded_password = ''
    for digit in password:
        digit = int(digit)
        if digit < 7:
            digit += 3
        elif digit == 7:
            digit = 0
        elif digit == 8:
            digit == 1
        elif digit == 9:
            digit == 2
        encoded_password = encoded_password + str(digit)
    return encoded_password


def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit ")
    print()


def main():
    menu_option = "none"
    while menu_option != 3:
        menu()
        menu_option = input("Please enter an option: ")
        if menu_option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        if menu_option == "2":
            pass

if __name__ == "__main__":
    main()