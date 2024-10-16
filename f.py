import base64

# Kode yang di-encode dalam Base64
encoded_code = """
Cgp4ID0gOAoKZm9yKGkgPSAwOyBpPD0xMDsgaSsrKXsKICAgaWYoaSA8PSB4KSB7CiAgICBjb25zb2xlLmxvZyhpKQogICAgaSArPSAxIAogICB9IGVsc2UgewogICAgY29uc29sZS5sb2coaSkKICAgfQoKfQo=
"""

def run_encoded_code(encoded_code):
    # Mendecode Base64
    decoded_code = base64.b64decode(encoded_code).decode('utf-8')
    
    # Menjalankan kode yang di-decode
    exec(decoded_code)

if __name__ == "__main__":
    run_encoded_code(encoded_code)