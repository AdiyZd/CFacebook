import requests

targer = "https://www.facebook.com/login.php"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://www.facebook.com/",
    "Origin": "https://www.facebook.com"
}

sessions = requests.Session()

payloads = {
    'email' : 'mulyono3031@gmail.com',
    'pass' : 'Adiganteng17'
}

response = sessions.post(url=targer, data=payloads, headers=headers)

if "d_user" in sessions.cookies:
    print("succesfully!")
else:
    print("Password and username wrong!")