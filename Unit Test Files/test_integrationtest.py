import unittest   # The test framework
import keygen   # Generates the keys
import encrypt_decrypt  # Encrypts and decrypts the file
import pathlib

# Integration test that tests the encrypt and decrypt functions after creating a new public and private key
# The decryption will fail if the keys are not generated properly


class Test_TestkeygenEncryptDecrypt(unittest.TestCase):

    def test_ALL_SQL(self):

        self.assertEqual(keygen.generateKeyPair(),
                         "Keys generated")  # Generate the keys

        self.assertEqual(encrypt_decrypt.encrypt(
            "DATABASE.sql", 'public.pem'), "DATABASE_encrypted.sql")  # Encrypt the file

        self.assertEqual(encrypt_decrypt.decrypt(pathlib.Path("DATABASE_encrypted.sql"), 'private.pem'),
                         'Decrypted file saved to DATABASE_encrypted.decrypted')  # Decrypt the file
        
    def test_ALL_LIBC(self):

        self.assertEqual(keygen.generateKeyPair(),
                         "Keys generated")  # Generate the keys

        self.assertEqual(encrypt_decrypt.encrypt(
            "aes_core.c", 'public.pem'), "aes_core_encrypted.c") # Encrypt the file

        self.assertEqual(encrypt_decrypt.decrypt(pathlib.Path("aes_core_encrypted.c"),
                         'private.pem'), 'Decrypted file saved to aes_core_encrypted.decrypted') # Decrypt the file


if __name__ == '__main__':
    unittest.main()
