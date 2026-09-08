# Cryptology Assignment 1
## Zoe Eigenbrod
## 9/7/26

#Program Specifications
**Language**: Python 
**Version**: 3.13.7

#Commands

##Generate key
```python3 xor_vigenere.py keygen --length <positive integer>```

##Encrypt
```python3 xor_vigenere.py encrypt --key <hex> --text <UTF-8 string>```

##Decrypt
```python3 xor_vigenere.py decrypt --key <hex> --ciphertext <hex>```

##Run test suite
```python3 -m unittest xor_vigenere_test_suite.py```

##Assumptions
* The environment that runs this has Python 3
* All integers entered are positive and non zero for length
* User follows commands provided

##Assistance
No outside help from generative AI tools were used.