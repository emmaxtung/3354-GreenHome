import unittest   # The test framework
import encrypt_decrypt   # The code to test
import pathlib

# Unit test that tests the encrypt and decrypt functions


class Test_TestEncryptDecrypt(unittest.TestCase):
    # SQL encrypt and decrypt
    def test_Encrypt_SQL(self):
        self.assertEqual(encrypt_decrypt.encrypt(
            "DATABASE.sql", 'public.pem'), "DATABASE_encrypted.sql")  # Encrypt the file

    def test_Decrypt_SQL(self):
        self.assertEqual(encrypt_decrypt.decrypt(pathlib.Path("DATABASE_encrypted.sql"),
                         'private.pem'), 'Decrypted file saved to DATABASE_encrypted.decrypted') # Decrypt the file 

    # C encrypt and decrypt using libcrypto C library file
    def test_Encrypt_LIBC(self):
        self.assertEqual(encrypt_decrypt.encrypt(
            "aes_core.c", 'public.pem'), "aes_core_encrypted.c") # Encrypt the file

    def test_Decrypt_LIBC(self):
        self.assertEqual(encrypt_decrypt.decrypt(pathlib.Path("aes_core_encrypted.c"),
                         'private.pem'), 'Decrypted file saved to aes_core_encrypted.decrypted') # Decrypt the file

if __name__ == '__main__':
    unittest.main()
