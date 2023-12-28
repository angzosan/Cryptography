# Cryptography
This contains various implementation of cryptography algorithms and solutions.


Wieners-Attack:
Simple demonstration of the Wiener's Attack, and against against the RSA encryption

Vigenere:
Implementation of the Vigenere Algorithm without key. Needs modification in order to be used for different texts.
Functions:
find_letter(arg): Corresponds the number given as an argument to a letter.
find_number(arg): Opposite of find_letter, corresponds the letter given as an argument to a number.
def given_frequency(arg): Returns the frequency of a number. This is a standard number.
#1 Finding the key length We count the coincidences and the number after which notive reoccurance or a pattern, is the key length. In this scenario, that number is 7. Although the number can be found, for now the number is passed hardcoded. For othertexts, this value needs to change.

Tonelli-Shanks
Script that finds the modular square root of two numbers. The script follows the Tonelli-Shanks algorithm which is widely used in cryptography.
Function pow1:
Function gcd: Recursice function that finds the gcd between two numbers.
Function order: Returns a number k such that b^k = 1 (mod p)
Function convertx2e:
Function STonelli: This function acts like th 'main' would in Java,C++ etc. It makes sure that all the nesessary conditions are met in ordetr for the rest of the functions to be called.


DivisorCheck->possibility.py
This program finds the possibility of a number with bit length n, having a integer divisor d with bit length betweet [n/2-1,n2+1]

The implementation is quite is and the main goal of this script is the familiarity with finding the divisors of a number.

The script consists of two parts. First, finding the divisors of a given number, and second the percentage of those divisors, whose value is between (n/2)-1 and (n/2)+1 where n is the bt=it length of the given number.

The function divisors(arg) is responsible for the first part. By simply checking whether the number mod i( = every number between one and n) equals to zero, and then appening an array which by the end will include all the divisors ( including 1 -> if that's not desired, change the range of the loop from range(1,m) to range(2,m) ).

Second to last, there's a counter that measures the numbers in the divisors array that are within the limits set earlier. Last but not lest, this number is divided by the total length of the array and we have the percentage.
