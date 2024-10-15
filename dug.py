import requests
from bs4 import BeautifulSoup

id = input("Masukan email anda : ")
key = input("Masukan password anda : ")

url = "https://www.facebook.com/login.php"

sessions = requests.Session()

response = sessions.get(url=url)
soup = BeautifulSoup(response.text, 'html.parser')

hidden = soup.find_all("input", type="hidden")

data = {input.get('name'): input.get('value') for input in hidden}

# data 
data = {
    'email' : id,
    'pass' : key
}

response = sessions.post(url=url, data=data)


if "user" not in response.url:
    print("login berhasil")

    # berikan cookies nya
    cok = sessions.cookies.get_dict()
    print("Cookies: ", cok)

    # lebih kompleks
    # dk_cok = ['dastr', 'sb', 'locale', 'vpd', 'm_pixel', 'wd', 'c_user', 'fr', 'xs', 'fbl_st', 'wl_cbv'] # agar kaya cookies dug masbro
    # compail = {cok: cookies.get(cok, "cokies 404") for cok in dk_cok}
    # print("cookies lengkap : \n ", compail)


else:
    print("username valid: \n ", response.text)