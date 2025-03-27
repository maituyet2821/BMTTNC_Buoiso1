from Crypto.Hash import SHA3_256

def sha3(message):
    sha3_hash = SHA3_256.new()  # Tạo đối tượng băm SHA-3
    sha3_hash.update(message)  # Cập nhật dữ liệu vào hash
    return sha3_hash.digest()  # Trả về giá trị băm

def main():
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')  # Nhập dữ liệu từ người dùng
    hashed_text = sha3(text)

    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    print("SHA-3 Hash:", hashed_text.hex())  # Chuyển đổi sang dạng hex để dễ đọc

if __name__ == "__main__":
    main()