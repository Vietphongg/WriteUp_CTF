def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():  # Chỉ dịch chuyển chữ cái
            shift_base = ord('A') if char.isupper() else ord('a')
            plaintext += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            plaintext += char  # Không thay đổi ký tự không phải chữ
    return plaintext


ciphertext = "CFX{Try_Caesar_Until_Correct_Flag_format}"  # Dữ liệu mã hóa
print("Brute-forcing Caesar cipher...")
for shift in range(1, 26):  # Thử từng bước dịch chuyển
    possible_plaintext = caesar_decrypt(ciphertext, shift)
    print(f"Shift {shift}: {possible_plaintext}")
