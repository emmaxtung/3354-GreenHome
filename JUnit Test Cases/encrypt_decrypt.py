import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
import pathlib

# Description: This program will encrypt and decrypt a file using RSA and AES


def encrypt(dataFile, publicKeyFile):
    with open(publicKeyFile, 'rb') as f:
        publicKey = f.read()
    # read data from file
    with open(dataFile, 'rb') as f:
        data = f.read()

    # convert data to bytes
    data = bytes(data)

    # create public key object
    key = RSA.import_key(publicKey)
    sessionKey = os.urandom(16)

    # encrypt the session key with the public key
    cipher = PKCS1_OAEP.new(key)
    encryptedSessionKey = cipher.encrypt(sessionKey)

    # encrypt the data with the session key
    cipher = AES.new(sessionKey, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    # save the encrypted data to file
    [fileName, fileExtension] = dataFile.split('.')
    encryptedFile = fileName + '_encrypted.' + fileExtension
    with open(encryptedFile, 'wb') as f:
        [f.write(x)
         for x in (encryptedSessionKey, cipher.nonce, tag, ciphertext)]
    return encryptedFile


def decrypt(dataFile, privateKeyFile):

    # read private key from file
    extension = dataFile.suffix.lower()
    with open(privateKeyFile, 'rb') as f:
        privateKey = f.read()
        # create private key object
        key = RSA.import_key(privateKey)

    # read data from file
    with open(dataFile, 'rb') as f:
        # read the session key
        encryptedSessionKey, nonce, tag, ciphertext = [
            f.read(x) for x in (key.size_in_bytes(), 16, 16, -1)]

    # decrypt the session key
    cipher = PKCS1_OAEP.new(key)
    sessionKey = cipher.decrypt(encryptedSessionKey)

    # decrypt the data with the session key
    cipher = AES.new(sessionKey, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    # save the decrypted data to file
    dataFile = str(dataFile)
    fileName = dataFile.split(extension)[0]
    fileExtension = '.decrypted'  # mark the file was decrypted
    decryptedFile = fileName + fileExtension
    with open(decryptedFile, 'wb') as f:
        f.write(data)

    return 'Decrypted file saved to ' + decryptedFile


if __name__ == '__main__':

    fileName = 'DATABASE.sql'   # file to encrypt
    enc_file = encrypt(fileName, 'public.pem')    # encrypt the file

    print('Encrypted file saved to ' + enc_file)
    print(decrypt(pathlib.Path(enc_file), 'private.pem'))  # decrypt the file
