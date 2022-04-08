import requests

BASE_URL = "http://aes.cryptohack.org/block_cipher_starter"

# 1) mendapatkan ciphertext dari enkripsi flag
r = requests.get(f"{BASE_URL}/encrypt_flag")
data = r.json()
ciphertext = data["ciphertext"]
print("ciphertext", ciphertext)

# 2) kirim ciphertext pada fungsi decrypt
r = requests.get(f"{BASE_URL}/decrypt/{ciphertext}")
data = r.json()
plaintext = data["plaintext"]
print("plaintext", plaintext)

# 3) konversi dari hex ke ASCII untuk mendapatkan flag
print("flag", bytearray.fromhex(plaintext).decode())

# flag is crypto{bl0ck_c1ph3r5_4r3_f457_!}