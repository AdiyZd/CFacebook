import os
import sys
import time
import requests
from bs4 import BeautifulSoup
import base64
import binascii

# warnanya masbro 
merah = "\033[31m"  # merah
MERAH = "\033[1;31m"  # MERAH ++
abang = "\033[38;5;1m"
putih = "\033[1;97m"  # putih
biru = "\033[34m"  # dark blue 
BIRU = "\033[94m"  # biru terang
hijau = "\033[32m"  # hijau
HIJAU = "\033[1;32m" # hijau ++
kuning = "\033[33m"  # kuning ++
KUNING = "\033[1;33m"  # kuning
ungu = "\033[35m"  # ungu ++
UNGU = "\033[1;35m"  # ungu ++

# berikan nilai default agar gak mbeleber
x = "\033[0m"  # default

url = "https://www.facebook.com/login.php"
p_sambut = "Welcome to script adiy"
tr = "Terimaksih telah menggunakan script adiy"
disk = ""

# taimer

def waktu(milisecond):
    while milisecond:
        # runing second
        mins, secs = divmod(milisecond, 60) # 60 mili
        timer = f"{mins:02d}:{secs:02d}" # mm:ss
        print(f"\r{timer}", end='')
        time.sleep(1) # delay 1 detik
        milisecond -= 1 # setipa loop kurangi 1 detik
        # print("\n") # biyar gak bentrok

def main():
    os.system("clear")
    os.system("cls") # opsional tergantung update di mana

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
    print(f"{BIRU} 1. Get cookies facebook")
    print(f"{BIRU} 2. Amankan password dengan encode")
    print(f"{BIRU} 3. Dekode password")
    print(f"{BIRU} 4. Dekode dokumen")
    print(f"{BIRU} 5. Encode ")
    print(f"{abang} 00. OUT!")

    # interaksi user 1
    print(f"{KUNING} WARNING {x} {putih}Pastikan pilihan anda benar!{x}")
    i_user_1 = input(f"{putih} Masukan pilihan anda dengan benar : {x}")

    #=================> bagian get cookies facebook <=================#
    if i_user_1 == "1":
        print(f"{putih} Silahkan masukan username dan password!")
        print(f"{KUNING} Pastikan akun tidak terkena cekpoin dan tidak ada sangkutan {putih}(A2F){x}")
        print(f"{putih}Autentikasi 2 faktor{x}")

        email = input(f"{putih}Masukan username / password :" + " ")
        key = input(f"{putih} Maukan password anda {x} :" + " ")

        session = requests.Session()

        response = session.get(url)
        ssid = BeautifulSoup(response.text, 'html.parser')

        b_transparan = ssid.find_all("input", type="hidden")

        data = {
            'email' : email,
            'pass' : key
        }
        
        response = session.post(url=url, data=data)

        # validasi user login
        if "user" not in response.url:
            print(f"{HIJAU} Sucessfully! {x}")

            d_cok = session.cookies.get_dict()
            print(f"{putih} Cookies anda adalah : \n {x}", d_cok)

            print(disk)

            print(f"{putih} Apakah anda ingin tetap berada di script adiy?{x}")
            print(f"{putih} Silahkan masukan y untuk melanjutkan dan n untuk out")

            ok = input(f"{putih} Masukan pilihan anda : ")

            if ok.lower() == "y":
                os.system("clear")
                print(f"{HIJAU} System akan siap dalam waktu {waktu(60)} detik {x}")
                main()
            # erikan kondisi agar system berhenti
            else:
                os.system("clear")
                print(f"{abang}{x}{tr}") # ambil nilai dari data
                waktu(120) # berikan nilai wktu
    
    #=================> bagian encode <=================#
    elif i_user_1 == "2":
        print(f"{KUNING} Warning : {x} {putih} Password bersifat privasi jadi ingat dengan benar!")
        print(f"{putih} Silahkan masukan password yang ingin anda encode {x}")
        print(f"{KUNING} Harus bersifat string{x}")

        user_encode = input(f"{putih} Silahkan masukan text yang ingin anda encode : {x}")
        print(f"{putih} Proses encode : ")
        # print(f"{waktu(10)}")

        # gass encode 

        e_di = base64.b64decode(user_encode.encode('utf-8'))
        di_encode = e_di.decode('utf-8')

        print(f"{HIJAU} Password berhasil di encode : {x} \n ", di_encode)


    else:
        os.system("clear")
        print(f"{abang} Pilihan tidak ada / tidak valid !{x}")
        print(f"{time.sleep(3)}{main()}")
main()
                