import base64

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

print("""\033[2;34m
                       ___......----:'"":--....(\\
                .-':'"":   :  :  :   :  :  :.(1\.`-.
              .'`.  `.  :  :  :   :   : : : : : :  .';
             :-`. :   .  : :  `.  :   : :.   : :`.`. a;
             : ;-. `-.-._.  :  :   :  ::. .' `. `., =  ;
             :-:.` .-. _-.,  :  :  : ::,.'.-' ;-. ,'''"
           .'.' ;`. .-' `-.:  :  : : :;.-'.-.'   `-'
    :.   .'.'.-' .'`-.' -._;..:---'''"~;._.-;
    :`--'.'  : :'     ;`-.;            :.`.-'`.
     `'"`    : :      ;`.;             :=; `.-'`.
  \033[1;37mv1.1.0\033[2;34m     : '.    :  ;              :-:   `._-`.
              `'"'    `. `.            `--'     `._;
                        `'"' 
\n\033[1;37mTHIS TOOL WAS PROGRAMMED BY TLER AL-SHAHRANI.\nPERSONAL WEBSITE : \033[1;34mhttps://tlersa.github.io/tleralshahrani/Index.html""")
print("\033[1;37m- "*35)

filename = input("\033[1;37m[\033[2;34m+\033[1;37m] - \033[1;37mEnter the filename : \033[2;34m")

option = input("""\033[1;37m[\033[2;34m1\033[1;37m] - Encode
\033[1;37m[\033[2;34m2\033[1;37m] - Decode
\033[1;37m[\033[2;34m+\033[1;37m] - \033[1;37mChoose : \033[2;34m""")

if option == "1":
    with open(filename, 'rb') as file: encoded_content = base64.b64encode(file.read())
    with open("New " + filename, "wb") as file: file.write(encoded_content)
    print("\033[1;32mThe file has been successfully encoded!")
elif option == "2":
    with open(filename, 'rb') as file: decoded_content = base64.b64decode(file.read())
    with open("New " + filename, "wb") as file: file.write(decoded_content)
    print("\033[1;32mThe file has been successfully decoded!")
else: print("\033[1;31mPlease choose 1 or 2!")
