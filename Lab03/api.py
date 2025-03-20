from flask import Flask, request, jsonify
from cipher.rsa import RSACipher  # Đảm bảo đường dẫn đúng
from cipher.ecc import ECCCipher
app = Flask(__name__)

# RSA CIPHER ALGORITHM
rsa_cipher = RSACipher()

@app.route('/api/rsa/generate_keys', methods=['GET'])
def rsa_generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({"message": "Keys generated successfully"})

@app.route("/api/rsa/encrypt", methods=["POST"])
def rsa_encrypt():
    data = request.json
    message = data.get("message", "").strip()
    key_type = data.get("key_type", "").strip()

    if not message:
        return jsonify({"error": "Message is required"}), 400
    if key_type not in ["public", "private"]:
        return jsonify({"error": "Invalid key type"}), 400

    private_key, public_key = rsa_cipher.load_keys()
    key = public_key if key_type == "public" else private_key
    encrypted_message = rsa_cipher.encrypt(message, key)
    
    return jsonify({"encrypted_message": encrypted_message.hex()})

@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    data = request.json
    ciphertext_hex = data.get("ciphertext", "").strip()
    key_type = data.get("key_type", "").strip()

    if not ciphertext_hex:
        return jsonify({"error": "Ciphertext is required"}), 400
    if key_type not in ["public", "private"]:
        return jsonify({"error": "Invalid key type"}), 400

    private_key, public_key = rsa_cipher.load_keys()
    key = public_key if key_type == "public" else private_key
    ciphertext_bytes = bytes.fromhex(ciphertext_hex)
    
    decrypted_message = rsa_cipher.decrypt(ciphertext_bytes, key)
    return jsonify({"decrypted_message": decrypted_message})

@app.route("/api/rsa/sign", methods=["POST"])
def rsa_sign_message():
    data = request.json
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"error": "Message is required"}), 400

    private_key, _ = rsa_cipher.load_keys()
    signature = rsa_cipher.sign(message, private_key)
    
    return jsonify({"signature": signature.hex()})

@app.route("/api/rsa/verify", methods=["POST"])
def rsa_verify_signature():
    data = request.json
    message = data.get("message", "").strip()
    signature_hex = data.get("signature", "").strip()

    if not message or not signature_hex:
        return jsonify({"error": "Message and signature are required"}), 400

    _, public_key = rsa_cipher.load_keys()
    signature_bytes = bytes.fromhex(signature_hex)
    is_verified = rsa_cipher.verify(message, signature_bytes, public_key)

    return jsonify({"is_verified": is_verified})


ecc_cipher = ECCCipher()

@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys():
    # Generate ECC keys
    ecc_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route('/api/ecc/sign', methods=['POST'])
def ecc_sign_message():
    # Get data from the request
    data = request.json
    message = data['message']

    # Load private key
    private_key, _ = ecc_cipher.load_keys()

    # Sign the message
    signature = ecc_cipher.sign(message, private_key)

    # Return the signature as hex
    signature_hex = signature.hex()
    return jsonify({'signature': signature_hex})

@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify_signature():
    # Get data from the request
    data = request.json
    message = data['message']
    signature_hex = data['signature']

    # Load keys
    public_key = ecc_cipher.load_keys()

    # Convert signature from hex to bytes
    signature = bytes.fromhex(signature_hex)

    # Verify the signature
    is_verified = ecc_cipher.verify(message, signature, public_key)

    return jsonify({'is_verified': is_verified})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
