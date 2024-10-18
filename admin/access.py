import requests

def get_access_token(username, password):
    login_url = "https://www.facebook.com/login.php"
    payload = {
        'email': username,
        'pass': password
    }
    with requests.Session() as session:
        response = session.post(login_url, data=payload)
        if response.ok and "c_user" in session.cookies:
            print("Login berhasil!")
            return session.cookies.get('xs')  # Mengambil token akses dari cookies
        else:
            print("Login gagal, periksa username dan password.")
            return None

# Menggunakan fungsi untuk mendapatkan token akses
username = input("Masukkan username: ")
password = input("Masukkan password: ")
access_token = get_access_token(username, password)

if access_token:
    user_info = get_user_info(access_token)
    print(user_info)
