# GREEN HOME TEST PLAN

## HOW TO RUN
This was created and tested on the open-source VSCode editor
https://code.visualstudio.com/

This is written in python 3.10.

The code uses the python crypto library to install

Use the following line to install the library

`pip install pycryptodome`

keygen.py creates the RSA private and public keys (PQC libraries were not workng so RSA was used)

These keys are stored in private.pem and public.pem
encrypt_decrypt.py is used to encrypt and decrypt the data using the public and private keys

The encrypted data is stored in has ``_encrypted`` appended to the file name

The decrypted data is stored in has ``decrypted`` appended to the file

The unit test is run using the following command in the terminal

`python -m unittest test_unittest.py`
    
The integration test is run using the following command in the terminal

`python -m unittest test_integrationtest.py`

You could also run the tests using the VSCode editor

## Description:

There are two test cases:
*   An unit test, test_unittest.py
*   An integration test, test_integrationtest.py


## Unit Test
The unit test is used to test the encrypt_decrypt.py file
The unit test tests the following functions:
*   encrypt()
*   decrypt()

## Integration Test
The integration test is used to test the entire system from the keygen.py file to the encrypt_decrypt.py file
The integration test tests the following functions:
*   generate_keys()
*   encrypt()
*   decrypt()

## Test Cases
The test cases use the following data:
*   A sample DATABASE written in sql
*   A sample source file from the openSSL library


    

