import requests
import re 

mCookies = input("Silahkan masukan cookies anda :" + " ").strip()

list_ck = mCookies.split(';')

cok = {}

for cookie in mCookies:
    if '=' in cok:
        key, value = cookie.strip().split('=', 1)
        cok[key] = value

cok_search = {key: cok[key] for key in ['c_user', 'xs'] if key in cok} 

# gass ambil nilai 
def get():
    try:
        # Kirim request ke Facebook dengan cookies
        response = requests.get("https://www.facebook.com/", cookies=cok)


        # Periksa apakah login berhasil (status code 200)
        if response.status_code == 200:
            print("Login berhasil.")

            # Cari USER_ID di dalam HTML response menggunakan regex
            id = re.search(r'"USER_ID":"(\d+)"', response.text)

            if id:
                # Ambil hasil dari group pertama dari regex
                facebook_id = id.group(1)
                print(f"Facebook ID: {facebook_id}")
            else:
                print("Facebook ID tidak ditemukan.")
        else:
            print(f"Login gagal. Status code: {response.status_code}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Pastikan fungsi dijalankan hanya saat script dijalankan langsung
if __name__ == "__main__":
    get()

