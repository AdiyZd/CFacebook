from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# Path ke ChromeDriver
chromedriver_path = 'path_to_chromedriver'  # Ganti dengan path ke ChromeDriver di sistem kamu

# Setup ChromeDriver menggunakan Service
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

# Buka halaman login Facebook
driver.get("https://www.facebook.com/login.php")

# Cari elemen input email dan password
email_input = driver.find_element_by_id("email")
password_input = driver.find_element_by_id("pass")

# Masukkan email dan password
email_input.send_keys("mulyono3031@gmail.com")
password_input.send_keys("Adiganteng17")

# Submit form
password_input.send_keys(Keys.RETURN)

# Tunggu sampai halaman login selesai
driver.implicitly_wait(5)

# Cek apakah login berhasil dengan memeriksa URL atau elemen halaman
if "login_attempt" not in driver.current_url:
    print("Login berhasil!")
else:
    print("Login gagal!")

# Tutup browser
driver.quit()
