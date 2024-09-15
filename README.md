# Vixhal
Vixhal is a Python library designed for secure key-value storage using AES encryption. It provides functionality for generating AES keys, encrypting and decrypting data, and converting between text and bytes. The library is designed for in-memory storage, making it suitable for fast, temporary data handling.

## Features
Secure AES encryption for key-value pairs.
Easy-to-use encryption and decryption functions.
In-memory storage for quick access.
Suitable for web development, app development, AI, and data science.
## Installation
Install the library via pip:

`pip install vixhal`

## Usage
After installing the vixhal library, you can use the following methods:

**1. generate_key():** Generates a random 256-bit AES key.

```
from vixhal import generate_key

key = generate_key()
print(f"Generated Key: {key.hex()}")
```
**2. encrypt_data(data: bytes, key: bytes) -> bytes** 

Encrypts the given data using AES encryption.

```
from vixhal import encrypt_data, generate_key

data = b"my secret data"
key = generate_key()
encrypted_data = encrypt_data(data, key)
print(f"Encrypted Data: {encrypted_data}")
```
**3. decrypt_data(encrypted_data: bytes, key: bytes) -> bytes**
  
   Decrypts the given AES-encrypted data.

```
from vixhal import decrypt_data

decrypted_data = decrypt_data(encrypted_data, key)
print(f"Decrypted Data: {decrypted_data}")
```
**4. text_to_bytes(text: str, size: Optional[int] = None) -> bytes**

   Converts text into bytes.

```
from vixhal import text_to_bytes

text = "hello world"
byte_data = text_to_bytes(text)
print(f"Byte Data: {byte_data}")
```
**5. bytes_to_text(byte_data: bytes) -> str**

  Converts bytes back into text, handling non-printable characters.

```
from vixhal import bytes_to_text

text = bytes_to_text(byte_data)
print(f"Text: {text}")
```
**6. store_entry(key: str, value: str, store: dict) -> None**

   Stores a key-value pair securely in the provided dictionary using AES encryption.

```
from vixhal import store_entry

store = {}
store_entry("my_key", "my_value", store)
```
**7. retrieve_entry(key: str, store: dict) -> Optional[str]**

   Retrieves a value for the given key from the dictionary, decrypting it in the process.

```
from vixhal import retrieve_entry

retrieved_value = retrieve_entry("my_key", store)
print(f"Retrieved Value: {retrieved_value}")
```

## In-Memory Storage
The Vixhal library stores data in RAM. This provides high performance for temporary data storage in scenarios where fast access is crucial. However, if you require persistent storage, you can extend this system by saving encrypted data to disk or a database.

## Where and How to Use
This library can be useful in the following fields:

* **Web Development:** Store and retrieve encrypted data for secure session management or token storage.

* **App Development:** Handle local encryption for secure storage of sensitive data in mobile or desktop applications.

* **Artificial Intelligence (AI):** Securely store and manage sensitive model configurations or parameters.

* **Data Science:** Protect confidential data or credentials while processing sensitive datasets or performing computations.


# Contribution

**Github:**  https://github.com/TheVixhal/vixhal

We welcome contributions! If you want to contribute:

 1. Fork the repository.

 2. Create a new branch `git checkout -b feature-branch`.

 3. Commit your changes `git commit -m "Add new feature`.

 4. Push to the branch `git push origin feature-branch`.

 5. Open a Pull Request.

Please ensure your code passes all the tests before submitting.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
