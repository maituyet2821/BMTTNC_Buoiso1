class TranspositionCipher:
    def encrypt(self, plain_text, key):
        # Tạo bảng các cột
        columns = [''] * key

        # Chia văn bản thành các cột
        for i in range(len(plain_text)):
            columns[i % key] += plain_text[i]
        
        # Ghép các cột lại thành chuỗi kết quả
        encrypted_text = ''.join(columns)
        return encrypted_text

    def decrypt(self, cipher_text, key):
        # Tính toán số ký tự trên mỗi cột
        num_cols = key
        num_rows = len(cipher_text) // num_cols
        if len(cipher_text) % num_cols != 0:
            num_rows += 1  # nếu có dư ký tự, tăng thêm 1 hàng

        # Tính số cột dư
        num_shaded_boxes = (num_cols * num_rows) - len(cipher_text)

        # Tạo bảng trống để lưu các cột
        grid = [''] * num_cols

        # Cập nhật các cột trong bảng
        col = 0
        for symbol in cipher_text:
            grid[col] += symbol
            col += 1
            if col == num_cols:
                col = 0

        # Tạo chuỗi decrypted_text từ các hàng trong bảng
        decrypted_text = ''
        for row in range(num_rows):
            for col in range(num_cols):
                # Kiểm tra nếu cột này có dữ liệu ở hàng `row`
                if row < len(grid[col]):
                    decrypted_text += grid[col][row]

        return decrypted_text
