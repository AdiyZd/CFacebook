import requests

def login_with_cookies():
    raw_cookies = input("Masukkan cookies Anda: ")
    cookies = {}
    
    # Mem-parsing cookies yang dimasukkan oleh user
    for cookie in raw_cookies.split(';'):
        if '=' in cookie:
            key, value = cookie.strip().split('=', 1)
            cookies[key] = value

    # Mengambil token akses dari cookies
    access_token = cookies.get('xs')  # Misalnya, menggunakan cookie xs sebagai token akses

    if access_token:
        user_info = get_user_info(access_token)
        if user_info:
            print(f"Username: {user_info['name']}, ID: {user_info['id']}, Followers: {user_info.get('followers_count', 'N/A')}")
        else:
            print("Tidak dapat mengambil informasi pengguna.")
    else:
        print("Token akses tidak ditemukan dalam cookies.")

def get_user_info(token):
    # URL untuk mengambil data pengguna
    url = f'https://graph.facebook.com/me?fields=id,name,followers_count&access_token={token}'
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")  # Tambahkan ini untuk debugging
        print(f"Response: {response.text}")  # Tambahkan ini untuk melihat detail error
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error saat mencoba mengambil informasi pengguna: {e}")
        return None

# Jalankan fungsi
login_with_cookies()
