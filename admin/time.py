import time

def countdown_timer(seconds):
    while seconds:
        # Menampilkan detik yang tersisa
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'  # Format MM:SS
        print(f'\rTimer: {timer}', end='')  # \r untuk overwrite baris
        time.sleep(1)  # Delay 1 detik
        seconds -= 1  # Kurangi 1 detik

    print("\nWaktu habis!")

# Contoh penggunaan, countdown dari 2 menit
countdown_timer(120)