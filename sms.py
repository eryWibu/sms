import requests
import os

os.system('clear')
# logo
print ('''
          \033[1;95m ╔═╗\033[1;97m ┬─┐ ┌─┐\033[1;95m ┌┬┐
           \033[1;95m╚═╗ \033[1;97m├─┘ ├─┤\033[1;95m │││
          \033[1;95m ╚═╝ \033[1;97m┴   ┴ ┴ \033[1;95m┴ ┴ 
 	  \033[1;97m [\33[31;1m Coded By ERI\033[1;97m ]''')
print ('   \033[1;97m IP      :\33[32;1m 103.144.169.231')
print ('   \033[1;97m Script\33[32;1m Spam Sms !!')
print ('   \033[1;97m Klik\33[32;1m CTRL z\033[1;97m (Untuk Berhenti) ')
print ('\n! Nomor Di Awali\33[36;1m 8xxx')

nomor = input('\33[36;1m[-\33[36;1m]\033[1;97m Nomor Target : ')
req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
if 'terkirim' in req:
    print ('[+] Spaming Success')
else:
    print ('[+] Spaming Gagal')
