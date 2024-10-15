import os
import sys
import time
import requests
from bs4 import BeautifulSoup

# warna
merah = "\033[31m"  # merah
MERAH = "\033[1;31m"  # MERAH ++
abang = "\033[38;5;1m"
putih = "\033[1;97m"  # putih
biru = "\033[34m"  # dark blue 
BIRU = "\033[94m"  # biru terang
hijau = "\033[32m"  # hijau
kuning = "\033[33m"  # kuning ++
KUNING = "\033[1;33m"  # kuning
ungu = "\033[35m"  # ungu ++
UNGU = "\033[1;35m"  # ungu ++

x = "\033[0m"  # default


os.system("cls")
print(f'{putih}WELLCOME BOLO DI SC ADIYZD\n')
print(f"""
{abang}░█████╗░██████╗░██╗██╗░░░██╗███████╗██████╗░
{abang}██╔══██╗██╔══██╗██║╚██╗░██╔╝╚════██║██╔══██╗
{abang}███████║██║░░██║██║░╚████╔╝░░░███╔═╝██║░░██║
{putih}██╔══██║██║░░██║██║░░╚██╔╝░░██╔══╝░░██║░░██║
{putih}██║░░██║██████╔╝██║░░░██║░░░███████╗██████╔╝
{putih}╚═╝░░╚═╝╚═════╝░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░  
{x}
""")

print(f"{putih}pilih opsi{x}")
print(f"{BIRU} 1. get cookies")
print(f"{KUNING} 2. cookies to pw")
print(f"{merah} 00. OUT!{x}")

user_interaksi = input(f"{putih}Masukan pilihan dana {x}: {kuning}")
time.sleep(5)
os.system("cls")
print(f"{x} Silahkan tunggu sebentar, system sedang bersiap!")
os.system("cls")

if user_interaksi == "1":
    print(f"{BIRU}system belom di tambahkan!{x}")
elif user_interaksi == "2":
    print(f"{KUNING}lagi dalam proses pengembangan{x}")
else:
    print(f"{MERAH}pilihan tidak valid{x}")