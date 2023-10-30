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



if __name__ == '__main__':
    while True:
        stored = ""
        old = ""
        menu()
        ans = input("Please enter an option: ")
        if ans == "1":
            convert = input("Please enter your password to encode: ")
            if len(convert) != 8:
                raise ValueError("ERROR! Not 8 digits!")
            old += convert
            stored += encode(convert)
            print("Your password has been encoded and stored!")


