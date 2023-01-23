from connect import *
passwrd = input("Enter Your password: ")
encrypt_mode = int(input("Enter 1. To encrypt in type 7 algorithm or 2. To encrypt in MD5 algorithm: "))
if(encrypt_mode == 1):
    ssh_connect.send_command('enable password ' + passwrd)
    ssh_connect.send_command('service password-encryption')
elif(encrypt_mode == 2):
    ssh_connect.send_command('enable secret ' + passwrd)