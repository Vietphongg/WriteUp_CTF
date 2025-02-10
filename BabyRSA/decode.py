
from Cryptodome.Util.number import long_to_bytes

# Đọc private key
private_key_path = "private_key.pem"
with open(private_key_path, "r") as f:
    key_data = f.read().splitlines()

n = int(key_data[0])
d = int(key_data[1])

# Đọc ciphertext
ciphertext_path = "ciphertext.txt"
with open(ciphertext_path, "r") as f:
    ciphertext = int(f.read().strip())

# Giải mã
decrypted_int = pow(ciphertext, d, n)
decrypted_message = long_to_bytes(decrypted_int)

# Hiển thị kết quả
print(decrypted_message.decode(errors="ignore"))
