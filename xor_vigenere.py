import argparse
import secrets

#XOR operation
def xor_operation(message, key):

    if len(key) == 0:
        raise ValueError("invalid input")

    #byte object
    xor = b""
    for i in range(len(message)):
        #xor/compare byte from message and from key
        xor += bytes([message[i]^key[i % len(key)]]) #modulus key length for mismatch lengths
    
    return xor


def keygen(length):
    return secrets.token_bytes(length) #generate key with secrets


def hex_to_bytes(num):
    #check whitespace
    if num != num.strip():
        raise ValueError("invalid input")

    return bytes.fromhex(num)


def encrypt(key, text):
    message = text.encode("utf-8")
    return xor_operation(message, key)


def decrypt(key, ciphertext):
    message = xor_operation(ciphertext, key)
    return message.decode("utf-8")
   

def main():
    parser = argparse.ArgumentParser()
    #parser commands
    parser.add_argument("command")
    parser.add_argument("--length")
    parser.add_argument("--key")
    parser.add_argument("--text")
    parser.add_argument("--ciphertext")

    args = parser.parse_args()

    try:
        #key generation
        if args.command == "keygen":
            length = int(args.length) #convert input to int
            if length <= 0:
                raise ValueError("invalid length value")
            key = keygen(length)
            print(key.hex()) #output key as hexadecimal

        elif args.command == "encrypt":
            key = hex_to_bytes(args.key)

            if len(key) == 0:
                raise ValueError("key is empty")

            ciphertext = encrypt(key, args.text)
            print(ciphertext.hex())

        elif args.command == "decrypt":
            key = hex_to_bytes(args.key)
            ciphertext = hex_to_bytes(args.ciphertext)

            if len(key) == 0:
                raise ValueError("key is empty")
            print(decrypt(key, ciphertext))

        else:
            raise ValueError("invalid input")

    except (ValueError, UnicodeDecodeError) as error:
        parser.error(error)

    return 0


if __name__ == "__main__":
    main()