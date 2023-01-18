import sys

def parbaude(x):
    x = -1
    while x < 0 :
        try:
            x = int(input("rindu skaits: "))
        except:
            print("tas nav skaitlis")
        if x < 0:
           print("neder") 
    return x 
    


def pyr_apg(x):
    for i in range (x):
        print(" " * i + "#" * (x - i) + " " + "#" * (x - i))

def pyr_sym(x):
    sym = input("simbols: ")
    for i in range (x):
        print(" " * (x - i) + sym * (i + 1) + " " + sym * (i + 1))

def pyr_num(x):
    for i in range (x):
        n = str(i)
        print(" " * (x - i) + n * (i + 1) + " " + n * (i + 1))    


def pyr_alp(x):
    ascii_value = 65
    for i in range (x):
        n = chr(ascii_value)
        print(" " * (x - i) + n * (i + 1) + " " + n * (i + 1))   
        ascii_value += 1

def pyr_alp2(x):
    ascii_value = 65
    for i in range(x):
        for j in range(i+1):
            alphabet = chr(ascii_value)
            print( alphabet, end="")
            ascii_value += 1
        print("")



def full_prog():
    cmd = ""
    x = 0
    while(cmd!="s"):
        print("kadu piramidu man uzzimet?")
        print("1. apgriezto")
        print("2. ar simboliem")
        print("3. skaitlu")
        print("4. ar alfabetu")
        print("5. no alfabeta")
        cmd = input("Atbilde: ")
        if cmd == "1":
            x = parbaude(x)
            pyr_apg(x)
            cmd = ""
            while cmd != "1":
                print("")
                print("vel vienu?")
                print("1. ja")
                print("2. ne")
                cmd = input("Atbilde: ")
                if cmd == "1":
                    pass
                elif cmd == "2":
                    sys.exit()
        if cmd == "2":
            x = parbaude(x)
            pyr_sym(x)
            cmd = ""
            while cmd != "1":
                print("")
                print("vel vienu?")
                print("1. ja")
                print("2. ne")
                cmd = input("Atbilde: ")
                if cmd == "1":
                    pass
                elif cmd == "2":
                    sys.exit()
        if cmd == "3":
            x = parbaude(x)
            pyr_num(x)
            cmd = ""
            while cmd != "1":
                print("")
                print("vel vienu?")
                print("1. ja")
                print("2. ne")
                cmd = input("Atbilde: ")
                if cmd == "1":
                    pass
                elif cmd == "2":
                    sys.exit()
        if cmd == "4":
            x = parbaude(x)
            pyr_alp(x)
            cmd = ""
            while cmd != "1":
                print("")
                print("vel vienu?")
                print("1. ja")
                print("2. ne")
                cmd = input("Atbilde: ")
                if cmd == "1":
                    pass
                elif cmd == "2":
                    sys.exit()
        if cmd == "5":
            x = parbaude(x)
            pyr_alp2(x)
            cmd = ""
            while cmd != "1":
                print("")
                print("vel vienu?")
                print("1. ja")
                print("2. ne")
                cmd = input("Atbilde: ")
                if cmd == "1":
                    pass
                elif cmd == "2":
                    sys.exit()
full_prog()
