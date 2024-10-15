import base64
import binascii

# Meminta input dari user
dp_user = input("Masukkan string Base64: ")

# Coba decode dari Base64 dengan validasi
try:
    ed_bytes = base64.b64decode(dp_user, validate=True)  # validate=True memastikan input valid Base64
    
    try:
        # Mencoba mendecode sebagai teks UTF-8
        decoded_str = ed_bytes.decode('utf-8')
        print("Decoded string:", decoded_str)
    except UnicodeDecodeError:
        # Jika tidak bisa didecode ke UTF-8, berarti datanya biner
        print("Data yang didecode adalah biner, bukan teks.")
        with open("output_file.bin", "wb") as file:
            file.write(ed_bytes)
        print("Data biner telah disimpan sebagai 'output_file.bin'.")
except binascii.Error:
    print("Input yang dimasukkan bukan string Base64 yang valid.")
except Exception as e:
    print(f"Error: {e}")
