import hashlib

def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size=64)  # Tạo đối tượng băm BLAKE2 với độ dài 64 bytes
    blake2_hash.update(message)  # Cập nhật dữ liệu vào hash
    return blake2_hash.digest()  # Trả về giá trị băm

def main():
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')  # Nhập dữ liệu từ người dùng
    hashed_text = blake2(text)

    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    print("BLAKE2 Hash:", hashed_text.hex())  # Chuyển đổi sang dạng hex để dễ đọc

if __name__ == "__main__":
    main()