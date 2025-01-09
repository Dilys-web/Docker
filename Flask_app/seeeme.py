import secrets

secret_key = secrets.token_hex(32)  # Generates a 32-byte (256-bit) hex string
print(secret_key)
