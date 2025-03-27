import hashlib

def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256()  # Tạo đối tượng băm SHA-256
    sha256_hash.update(data.encode('utf-8'))  # Chuyển đổi dữ liệu thành bytes và băm
    return sha256_hash.hexdigest()  # Trả về giá trị băm dưới dạng chuỗi hex

# Nhập dữ liệu từ người dùng
data_to_hash = input("Nhập dữ liệu để hash bằng SHA-256: ")
hash_value = calculate_sha256_hash(data_to_hash)

# In ra giá trị băm
print("Giá trị hash SHA-256:", hash_value)
