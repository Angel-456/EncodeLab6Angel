# Angel Maldonado
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")



def encode(code):
    new = ""
    for i in code:

        change = (int(i) + 3) % 10
        secret = str(int(change))
        new += secret
    return new


# Defines function to decode user's password
def decoder(password):
    string = ''
    for i in range(len(password)):
        # Shifts each digit down by 3 in password
        string = string + str(int(password[i]) - 3)
    return string


if __name__ == '__main__':
    while True:
        # adds epmty string for decoded
        stored = ""
        # adds empty string for encoded
        old = ""
        menu()
        ans = input("Please enter an option: ")
        if ans == "1":
            convert = input("Please enter your password to encode: ")
            if len(convert) != 8:
                raise ValueError("ERROR! Not 8 digits!")
            # adds values to empty strigs
            old += str(convert)
            stored += str(encode(convert))
            print("Your password has been encoded and stored!")
        if ans == "2":
            print("The encoded password is", stored, " and the original password is ", old, )
        if ans == "3":
            # quits program if optio 3 is selected.
            break
