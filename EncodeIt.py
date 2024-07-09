import marshal, os, time, base64

Black = "\033[1;30m"
Red = "\033[1;31m"
Green = "\033[1;32m"
Yellow = "\033[1;33m"
Blue = "\033[1;34m"
Purple = "\033[1;35m"
Cyan = "\033[1;36m"
White = "\033[1;37m"
Gray = "\033[1;39m"
DarkRed = "\033[2;31m"
DarkBlue = "\033[2;34m"
DarkPink = "\033[2;35m"
DarkCyan = "\033[2;36m"

print("""\033[1;36m
  ad8888888888ba
 dP'         `'8b,
 8  ,aaa,       'Y888a     ,aaaa,     ,aaa,  ,aa,
 8  8' `8           '88baadP''''YbaaadP'''YbdP''Yb
 8  8   8              '''        '''      ''    8b
 8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
 8  `''''       ,d8''
 Yb,         ,ad8'             \033[1;32mv2.2.0\033[1;36m
  'Y8888888888P'


\033[1;37mTHIS TOOL WAS PROGRAMMED BY TLER AL-SHAHRANI.
PERSONAL WEBSITE : \033[1;36mhttps://tlersa.github.io/tleralshahrani/Index.html""")
print("\033[1;37m- "*35)

def main_menu():
    print("""\033[1;37m[\033[1;36m01\033[1;37m] - Encode
\033[1;37m[\033[1;36m02\033[1;37m] - Decode

[\033[1;36m98\033[1;37m] - Report A Bug
[\033[1;36m99\033[1;37m] - Help
[\033[1;36m00\033[1;37m] - Exit""")

def submenu1():
    print("""\033[1;37m[\033[1;36m01\033[1;37m] - Codes Encode Only
\033[1;37m[\033[1;36m02\033[1;37m] - Public Encrypted For Sec

[\033[1;36m99\033[1;37m] - Back""")

def handle_selection(selection):
    if selection == "1" or selection == "01" or selection == "Encode" or selection == "DNCODE" or selection == "encode":
        submenu1()
        user_input = input("Choose : \033[1;36m")

        if user_input == "1" or user_input == "01" or user_input == "Encode To Hide Codes" or user_input == "ENCODE TO HIDE CODES" or user_input == "encode to hide codes":
            filename = input("\033[1;37mEnter the filename : \033[1;36m")

            print("\033[1;37mEncoding...")
            time.sleep(3)

            open_file = open(filename, 'r').read()

            compile_file = compile(open_file, '', 'exec')

            encode_file = marshal.dumps(compile_file)

            encode_code = open(f"Encoded {str(filename)}", 'w')

            encode_code.write('import marshal\nexec(marshal.loads('+repr(encode_file)+'))')

            print(f"""\n\033[1;37m[\033[1;32m✓\033[1;37m] The file has been successfully encoded!
The encoding was saved in {os.getcwd()}\Encoded {filename}\033[1;37m""")

        elif user_input == "2" or user_input == "02" or user_input == "Public Encrypted For Sec" or user_input == "PUBLIC ENCRYPTED FOR SEC" or user_input == "public encrypted for sec":
            filename = input("\033[1;37mEnter the filename : \033[1;36m")

            print("\033[1;37mEncrypting...")
            time.sleep(3)

            with open(filename, 'rb') as file: encoded_content = base64.b64encode(file.read())
            with open(f"Encoded {filename}", "wb") as file: file.write(encoded_content)

            print(f"""\n\033[1;37m[\033[1;32m✓\033[1;37m] The file has been successfully encoded!
The encoding was saved in {os.getcwd()}\Encoded {filename}\033[1;37m""")

        else: print("\033[1;31mPlease choose a valid option!\033[1;37m")

        another_operation = input("\n\033[1;37mWould u like another operation? (\033[1;36mY\033[1;37m/\033[1;36mN\033[1;37m) \033[1;36m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else:
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()

    elif selection == "2" or selection == "02" or selection == "Decode" or selection == "DECODE" or selection == "decode":
        filename = input("\033[1;37mEnter the filename : \033[1;36m")

        print("\033[1;37mDecoding...")
        time.sleep(3)

        with open(filename, 'rb') as file: decoded_content = base64.b64decode(file.read())
        with open(f"Decoded {filename}", "wb") as file: file.write(decoded_content)

        print(f"""\n\033[1;37m[\033[1;32m✓\033[1;37m] The file has been successfully decoded!
The decoding was saved in {os.getcwd()}\Decoded {filename}\033[1;37m""")

        another_operation = input("\n\033[1;37mWould u like another operation? (\033[1;36mY\033[1;37m/\033[1;36mN\033[1;37m) \033[1;34m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else: 
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()

    elif selection == "98" or selection == "Report A Bug" or selection == "REPORT A BUG" or selection == "rebort a bug":
        print("""\n\033[1;37mContact me through one of my acc
all my acc : \033[1;36mhttps://tlersa.github.io/tleralshahrani/Index.html#contact""")

        another_operation = input("\n\033[1;37mWould u like another operation? (\033[1;36mY\033[1;37m/\033[1;36mN\033[1;37m) \033[1;36m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else:
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()

    elif selection == "99" or selection == "Help" or selection == "HELP" or selection == "help":
        print("""\n\033[1;37mContact me through one of my acc
all my acc : \033[1;36mhttps://tlersa.github.io/tleralshahrani/Index.html#contact""")

        another_operation = input("\n\033[1;37mWould u like another operation? (\033[1;36mY\033[1;37m/\033[1;36mN\033[1;37m) \033[1;36m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else:
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()

    elif selection == "00" or selection == "Exit" or selection == "EXIT" or selection == "exit": exit("\033[1;37m")

    else: print("\033[1;31mPlease choose a valid option!\033[1;37m")

def main():
    main_menu()

    while True:
        user_input = input("\033[1;37mChoose : \033[1;36m")
        handle_selection(user_input)

if __name__ == "__main__": main()
