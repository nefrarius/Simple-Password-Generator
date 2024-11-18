import random
import os

characters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',  
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',  
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',  
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', 
    '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '/', '?', '~', '`' 
]


def save_password(route, password):
    file = open(route+"/password.txt", "w")
    file.write(password+ os.linesep)
    file.write("---------------------"+ os.linesep)
    file.close()

os.system("cls||clear")
print(" ____   __   ____  ____  _  _   __  ____  ____     ___  ____  __ _ ")
print("(  _ \\ / _\\ / ___)/ ___)/ )( \\ /  \\(  _ \\(    \\   / __)(  __)(  ( \\")
print(" ) __//    \\\\___ \\\\___ \\\\ \\/ /(  O ))   / ) D (  ( (_ \\ ) _) /    /")
print("(__)  \\_/\\_/(____/(____/(_/\\_) \\__/(__\\_)(____/   \\___/(____)\\_)__)")






length = int(input("Length of the password?:"))
password = ''.join(random.choices(characters, k = length))
print("The generated password is "+password)

save = input("Do you want to sabe it in a .txt?(y/n):")


if save == "y":
    route = input("Where?(ex:/home/user/Desktop/):")
    save_password(route, password)
    print("Password saved in "+ route +"/password.txt")
elif save == "n":
        print("The password hasnt been saved")
else :
    print("The password hasnt been saved")
