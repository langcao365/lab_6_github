def encode(passwd):
    data = []
    for c in passwd:
        newc = str((int(c) + 3) % 10)
        data.append(newc)
    return "".join(data)

def decode(passwd):
    pass
    return 0 # this is a placeholder

running = True
encpass = 0
while running:
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit
""")
    option = input("Please enter an option:")
    if option == "1":
        p = input("Please enter your password to encode: ")
        encpass = encode(p)
        del p
        print("Your password has been encoded and stored!")
    elif option == "2":
        print(f"The encoded password is {encpass}, and the original password is {decode(encpass)}")
    elif option == "3":
        running = False

        
    
    
