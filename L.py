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


# data 
url = "https://www.facebook.com/login.php"

# lanjut Banner
def banner():
    while banner:
        os.system("clear")
        print(f"{putih} Wellcome to get cookies adi")
        print(f"Silahkan masukan pilihan anda di bawah{x}")
        print(f"""
        {abang}░█████╗░██████╗░██╗██╗░░░██╗███████╗██████╗░{x}
        {abang}██╔══██╗██╔══██╗██║╚██╗░██╔╝╚════██║██╔══██╗{x}
        {abang}███████║██║░░██║██║░╚████╔╝░░░███╔═╝██║░░██║{x}
        {putih}██╔══██║██║░░██║██║░░╚██╔╝░░██╔══╝░░██║░░██║
        {putih}██║░░██║██████╔╝██║░░░██║░░░███████╗██████╔╝
        {putih}╚═╝░░╚═╝╚═════╝░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░  
        {x}
        """)

        # pilihan nya 
        print(f"{BIRU} 1. Get cookies facebook")
        print(f"{BIRU} 2. Amankan password dengan encode")
        print(f"{BIRU} 3. Dekode password")
        print(f"{BIRU} 4. Dekode dokumen")
        print(f"{BIRU} 5. Encode ")
        print(f"{abang} 00. OUT!")

        # input user
        i_user = input(f"{putih}Masukan pilihan anda {KUNING} :")
        print(f"{putih} Pastikan pilihan anda benar {x}")

        #=================> bagian get cookies facebook <=================#
        # eksekusi code
        if i_user == "1":
            print(f"{putih} Silahkan masukan username dan password!")
            print(f"Passtikan akun terhindar dari (A2F) autentikasi 2 faktor{x}")

            id = input(f"{putih}Masukan username / gmail : ")
            key = input(f"Masukan password : {x}")

            # eksekusi 
            sessions = requests.Session()

            response = sessions.get(url=url)
            soup = BeautifulSoup(response.text, 'html.parser')

            hidden = soup.find_all("input", type="hidden")

            data = {
                'email' : id,
                'pass' : key
            }


            response = sessions.post(url=url, data=data)

            # kondisi apakah password benar 

            if "info_user" not in response.url:
                print(f"{HIJAU} SUCESSFULLY! {x}")

                # berikan cookeis nya 
                adi_jancok = sessions.cookies.get_dict()
                print(f"{putih} Cookies anda : {x} :\n ", adi_jancok)

                print("")

                # inteaksi user ke 2
                print(f"{putih} apakah anda ingin cek lagi?")
                print("")
                print(f"Masukan y jika ingin cek lagi dan n untuk keluar")

                ok = input("Silahkan masukan pilihan anda : ")

                # kondisi ke 3

                if ok.lower() == "y":
                    os.system("clear")
                    print(f"{putih} system akan siap dalam 5 detik")
                    time.sleep(4)

                else:
                    os.system("clear")
                    print(f"{putih}Terimakasih telah menggunakan sc adiy get cookies :) ")
                    print(f"babay kawan")
                    print(f"perintah akan berhenti dalam 11 detik ! {x}")              
                    time.sleep(10)

                    # biyar keluar
                    break


            else:
                print(f"{abang} Akun tidak berhasil login! {x}")
                print(f"{putih} Silahkan ganti atau cek ulang password anda")

        #=================> bagian encode <=================#
        elif i_user == "2":
            print(f"{putih} Passeord bersifat rahasia jadi ingat ingat dengan benar{x}")
            print(f"{putih} Silahkan masukan password di bawah{x}")
            print("")

            # berikan interaksi ke user 
            d_user = input(f"{putih} Masukan password yang madu di encode : {x}")

            # eksekusi code nya
            e_adiy = base64.b64encode(d_user.encode('utf-8'))
            encode_str = e_adiy.decode('utf-8')
            # kasih encode nya mas
            print(f"{hijau} Hasil pengamanan code anda adalah : \n {putih}", encode_str)

            # kasih jeda agar lop gak berjalan terus

            d_encode = input(f"{putih} Apakah anda ingin tetap di script saya (y/n) : ")

            if d_encode.lower() == "y":
                os.system("clear")
                print(f"{putih} System akan siap dalam waktu 5 detik")
            # kondisi jika n
            else:
                os.system("clear")
                print(f"{abang} Terimakasih telah menggunakan secript adiy")
                print(f"system akan siap dalam waktu 10detik ")
                time.sleep(9)

        #=================> bagian decode <=================#

        if i_user == "3":
            print(f"{putih} Decode password by adiy")
            print(f"Silahkan masukan encode password anda{x}")


            decode = input(f"{putih}Masukan password yang ingin di decode : ")

            try:
                adiy_decode = base64.b64decode(decode, validate=True)
                
                # eksekusi yang ke 2
                try:
                    # decode dengan utf-8
                    decode_str = adiy_decode.decode('utf-8')
                    print(f"{hijau} text berhasil di decode : {x}", decode_str)

                    # agar gak infinity
                    ui_in = input(f"{putih} Apakah anda ingin lanjut (y/n) :" + " ")

                    # kondisi agar back
                    if ui_in.lower() == "y":

                        # bersihkan halaman
                        os.system("clear")
                        print(f"{putih} System akan siap dalam waktu 5 detik")
                        time.sleep(4)

                    else:
                        os.system("clear")
                        print(f"{abang} Terimakasih telah menggunakan script adi {x}")
                        print(f"{putih}System akan membersihkan terminal anda dalam waktu 5 detik{x}")
                        print(f"{putih} Silahkan ditunggu {x}")
                        time.sleep(4)


                except UnicodeTranslateError:
                    # decode 
                    print(f"{abang} Data yang ingin di encode salah! atau data bersifat number")
                    with open("encode_adi_ganteng.bin", "wb") as file:
                        file.write(adiy_decode)
                    print(f"{putih} Data bin telah di simpan sebagai encode_adi_ganteng.bin")

                    # interaksi jika true 
                    print(f"{putih} Silahkan di simpan dengan benar password nya")
                    print(f"Ketik (y/n) jika ingin lanjut{x}")
                    
                    
                    # opsional 
                    # opsi2 = input("apakah anda ingin lanjut (y/n)")

                    # if opsi2.lower() == "y":
                    #     os.system("clear")
                    #     runing = False
                    #     print("system akan segera siap silahkan tunggu sebentar")
                    #     time.sleep(5)
                    # else:
                    #     os.system("clear")
                    #     print(f"{abang}Terimaksih telah menggunakan script adiy {x}")
                    #     time.sleep(5)
                    #     break

            except binascii.Error:
                print(f"{abang} Masukan string bukan number masbroo")
            except Exception as e:
                print(f"{abang} Error {x}: {e}")
                time.sleep(5)



        elif i_user == "00":
            runing = False
            print(f"{putih}Terimaksih telah menggunakan script adiy{x}")


        else:
            os.system("clear")
            print(f"{abang} Pilihan tidak valid silahkan coba lagi")
            time.sleep(3)


if __name__ == "__main__":
    banner()



