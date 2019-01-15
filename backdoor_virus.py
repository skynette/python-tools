import os
import time
'''
Custom python virus that run once computer logs on
Still needs a lot of work
'''
username = os.getlogin()
print ("\t\t\t[!] Changing Directory.....")
time.sleep(2)
os.chdir("C:\\Users\\"+username+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
print ('\t\t\t[+] Making directory.....')
time.sleep(2)
# os.rmdir("Test.txt")
os.mkdir("Test.txt")
print ("             __   __  _____  _     _ . _    _ _______      ______  _______ _______ __   _")
print ("   \_/   |     | |     | '  \  /  |______      |_____] |______ |______ | \  |")
print ("    |    |_____| |_____|     \/   |______      |_____] |______ |______ |  \_|")
print ("                                                                             ")
print ("               _     _ _______ _______ _     _ _______ ______               ")
print ("                |_____| |_____| |       |____/  |______ |     \              ")
print ("                |     | |     | |_____  |    \_ |______ |_____/          ")
print(os.listdir())
input()