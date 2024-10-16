import os
import sys 
import time
import base64 
import binascii

def banner():
    running = True  # Flag untuk mengontrol kapan loop harus berhenti
    while running:
        os.system("clear")
        print(f" Wellcome to get cookies adi")
        print(f"Silahkan masukan pilihan anda di bawah")
        print(f"""
       ░█████╗░██████╗░██╗██╗░░░██╗███████╗██████╗░
        ██╔══██╗██╔══██╗██║╚██╗░██╔╝╚════██║██╔══██╗
        ███████║██║░░██║██║░╚████╔╝░░░███╔═╝██║░░██║
        ██╔══██║██║░░██║██║░░╚██╔╝░░██╔══╝░░██║░░██║
        ██║░░██║██████╔╝██║░░░██║░░░███████╗██████╔╝
        ╚═╝░░╚═╝╚═════╝░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░  
        """)

        print(f" 1. Get cookies facebook")
        print(f" 2. Amankan password dengan encode")
        print(f" 3. Dekode password")
        print(f" 4. Dekode dokumen")
        print(f" 5. Encode ")
        print(f" 00. OUT!")

        # input user
        i_user = input(f"Masukan pilihan anda  :")
        print(f" Pastikan pilihan anda benar ")

        # Eksekusi pilihan
        if i_user == "1":
            # Bagian get cookies facebook
            pass  # Kode yang sudah kamu buat

        elif i_user == "2":
            # Bagian encode
            pass  # Kode yang sudah kamu buat

        elif i_user == "3":
            print(f" Decode password by adiy")
            print(f"Silahkan masukan encode password anda")

            decode = input(f"Masukan password yang ingin di decode : ")

            try:
                adiy_decode = base64.b64decode(decode, validate=True)
                
                try:
                    decode_str = adiy_decode.decode('utf-8')
                    print(f" text berhasil di decode : ", decode_str)
                except UnicodeTranslateError:
                    print(f" Data yang ingin di encode salah! atau data bersifat number")
                    with open("encode_adi_ganteng.bin", "wb") as file:
                        file.write(adiy_decode)
                    print(f" Data bin telah di simpan sebagai encode_adi_ganteng.bin")
                
                # Interaksi tambahan untuk pengguna
                lanjut = input(f" Apakah ingin lanjut? (y/n): ")
                if lanjut.lower() != "y":
                    running = False  # Set flag untuk menghentikan loop
                    print(f"Terima kasih telah menggunakan script! ")

            except binascii.Error:
                print(f" Masukan string bukan number masbroo")
            except Exception as e:
                print(f" Error : {e}")

        elif i_user == "00":
            running = False  # User memilih keluar, hentikan loop
            print(f" Keluar dari sistem... ")

        else:
            print(f" Pilihan tidak valid, coba lagi! ")
