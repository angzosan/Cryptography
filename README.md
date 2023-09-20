# Cryptography
This package contains various implementation of cryptography algorithms and solutions.


Wieners-Attack:
Simple demonstration of the Wiener's Attack, and against against the RSA encryption

Vigenere:
Implementation of the Vigenere Algorithm without key. Needs modification in order to be used for different texts.
Functions:
find_letter(arg): Corresponds the number given as an argument to a letter.
find_number(arg): Opposite of find_letter, corresponds the letter given as an argument to a number.
def given_frequency(arg): Returns the frequency of a number. This is a standard number.
#1 Finding the key length We count the coincidences and the number after which notive reoccurance or a pattern, is the key length. In this scenario, that number is 7. Although the number can be found, for now the number is passed hardcoded. For othertexts, this value needs to change.

Pseudroprime-and-Carmichael
Scripts that detect : 1. If a number is a carmichael number 2. if a number is pseudoprime or not. Carmichael Numbers: A Carmichael number will pass a Fermat primality test to every base b relatively prime to the number, even though it is not actually prime. ![image](https://user-images.githubusercontent.com/118728873/212889467-b59e754c-8df4-43a4-921f-f7f5b3977619.png)
or 
![image](https://user-images.githubusercontent.com/118728873/212889562-f8fe7033-0fcb-4c3d-8c04-feb8a5b05bf1.png)

Pseudoprime numbers: A pseudoprime is a probable prime (an integer that shares a property common to all prime numbers) that is not actually prime. Pseudoprimes are classified according to which property of primes they satisfy.

ImageEncryptionDecryption
Script that encrypts and decrypts an image in Python
Input: 
 1. The path of the image ( currently it's commented out)
 2. The key
Function : encr_decryc
It's responsible for the encryption/decription of the image.


CRC - Cyclic redundancy check
Error-detecting code commonly used in digital networks and storage devices to detect accidental changes to digital data. Blocks of data entering these systems get a short check value attached, based on the remainder of a polynomial division of their contents. On retrieval, the calculation is repeated and, in the event the check values do not match, corrective action can be taken against data corruption( Wikipedia )

Tonelli-Shanks
Script that finds the modular square root of two numbers. The script follows the Tonelli-Shanks algorithm which is widely used in cryptography.
Function pow1:
Function gcd: Recursice function that finds the gcd between two numbers.
Function order: Returns a number k such that b^k = 1 (mod p)
Function convertx2e:
Function STonelli: This function acts like th 'main' would in Java,C++ etc. It makes sure that all the nesessary conditions are met in ordetr for the rest of the functions to be called.
