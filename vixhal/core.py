import os
from typing import Dict, Tuple, Optional
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Constants
AES_KEY_SIZE = 32  # AES-256

def generate_key() -> bytes:
    """Generate a random AES key."""
    return get_random_bytes(AES_KEY_SIZE)

def encrypt_data(data: bytes, key: bytes) -> bytes:
    """Encrypt data using AES."""
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))
    return cipher.iv + ciphertext  # Prepend IV for use in decryption

def decrypt_data(encrypted_data: bytes, key: bytes) -> bytes:
    """Decrypt data using AES."""
    iv = encrypted_data[:AES.block_size]
    ciphertext = encrypted_data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size)

def store_entry(key: str, value: str, store: Dict[str, Tuple[bytes, bytes]]) -> None:
    """Store an entry securely."""
    if not key or not value:
        raise ValueError("Key and value must not be empty")
    
    aes_key = generate_key()  # Generate a new key for each entry
    value_bytes = text_to_bytes(value)
    encrypted_value = encrypt_data(value_bytes, aes_key)
    
    store[key] = (aes_key, encrypted_value)

def retrieve_entry(key: str, store: Dict[str, Tuple[bytes, bytes]]) -> Optional[str]:
    """Retrieve a stored entry."""
    if not key:
        raise ValueError("Key must not be empty")
    
    entry = store.get(key)
    if not entry:
        return None
    
    aes_key, encrypted_value = entry
    try:
        value_bytes = decrypt_data(encrypted_value, aes_key)
        return bytes_to_text(value_bytes)
    except (ValueError, KeyError):
        return None

def text_to_bytes(text: str, size: Optional[int] = None) -> bytes:
    """Convert text to bytes, optionally padded to a specified size."""
    byte_data = text.encode('utf-8')
    if size is not None:
        return byte_data.ljust(size, b'\x00')[:size]
    return byte_data

def bytes_to_text(byte_data: bytes) -> str:
    """Convert bytes to text, handling non-printable characters."""
    try:
        return byte_data.decode('utf-8').rstrip('\x00')
    except UnicodeDecodeError:
        return ''.join(chr(b) if 32 <= b < 127 else '?' for b in byte_data)
