import marshal, pyfiglet, os

try:
    import marshal, pyfiglet, os
except ModuleNotFoundError:
    os.system("pip install marshal")
    os.system("pip install pyfiglet")
    os.system("pip install os")
    
    os.system("clear")

#--------------------------------
Black = "\033[1;30m"       #Black
Red = "\033[1;31m"         #Red
Green = "\033[1;32m"       #Green
Yellow = "\033[1;33m"      #Yellow
Blue = "\033[1;34m"        #Blue
Purple = "\033[1;35m"      #Purple
Cyan = "\033[1;36m"        #Cyan
White =" \033[1;37m"       #White
Gray = "\033[1;39m"        #Gray
DarkRed = "\033[2;31m"     #Dark Red
DarkBlue = "\033[2;34m"    #Drak Blue
DarkPink = "\033[2;35m"    #Dark Pink
DarkCyan = "\033[2;36m"    #Dark Cyan
#--------------------------------

print("""\033[1;33m
 _______   ________           ________ ___  ___       _______   ________      
|\  ___ \ |\   ___  \        |\  _____\\  \|\  \     |\  ___ \ |\   ____\     
\ \   __/|\ \  \\ \  \       \ \  \__/\ \  \ \  \    \ \   __/|\ \  \___|_    
 \ \  \_|/_\ \  \\ \  \       \ \   __\\ \  \ \  \    \ \  \_|/_\ \_____  \   
  \ \  \_|\ \ \  \\ \  \       \ \  \_| \ \  \ \  \____\ \  \_|\ \|____|\  \  
   \ \_______\ \__\\ \__\       \ \__\   \ \__\ \_______\ \_______\____\_\  \ 
    \|_______|\|__| \|__|        \|__|    \|__|\|_______|\|_______|\_________\
                                                                  \|_________| """)
print("\033[1;37mThis Tool Was Programmed By : TLER AL-BISHI \nWebsite For All Accs : \033[1;34mhttps://linktr.ee/tler.sa")
print("\033[1;37m- "*25)

filee = input("\033[1;37m[\033[1;33m+\033[1;37m] - \033[1;31mWrite The File Name Or Path \033[1;37m: \033[1;31m")

open_file = open(filee, 'r').read()

compile_file = compile(open_file, '', 'exec')

encrypt_file = marshal.dumps(compile_file)

encrypt_code = open('New_'+str(filee), 'w')

encrypt_code.write('import marshal\nexec(marshal.loads('+repr(encrypt_file)+'))')

print("\033[1;32mThe File Has Been Successfully Encrypted! \033[1;37m: "+str(filee))
