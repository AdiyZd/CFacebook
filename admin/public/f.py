import requests

def get_access_token(app_id, app_secret, redirect_uri, code):
    url = 'https://graph.facebook.com/v12.0/oauth/access_token'
    params = {
        'client_id': app_id,
        'client_secret': app_secret,
        'redirect_uri': redirect_uri,
        'code': code
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print('Error getting access token:', response.text)
        return None

def get_user_info(access_token):
    url = 'https://graph.facebook.com/me'
    params = {
        'access_token': access_token,
        'fields': 'id,name,email'  # Anda bisa menambahkan field lain yang diperlukan
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print('Error getting user info:', response.text)
        return None

def main():
    app_id = 'YOUR_APP_ID'  # Ganti dengan App ID Anda
    app_secret = 'YOUR_APP_SECRET'  # Ganti dengan App Secret Anda
    redirect_uri = 'YOUR_REDIRECT_URI'  # Ganti dengan Redirect URI Anda
    code = input("Masukkan kode otorisasi: ")  # Dapatkan kode dari URL pengalihan

    access_token = get_access_token(app_id, app_secret, redirect_uri, code)
    if access_token:
        user_info = get_user_info(access_token)
        print('User Info:', user_info)
    else:
        print('Gagal mendapatkan token akses')

if __name__ == "__main__":
    main()
