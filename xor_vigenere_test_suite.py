import unittest
from xor_vigenere import xor_operation, encrypt, decrypt, keygen, hex_to_bytes


class Test(unittest.TestCase):

    def test_round_trip(self):
        key = b"key"
        message = "test"
        self.assertEqual(decrypt(key, encrypt(key, message)), message)


    def test_answer_1(self):
        key = bytes.fromhex("494345")
        message = bytes.fromhex("41747461636b206174206461776e21")
        answer = bytes.fromhex("08373128202e6922316927243e2d64")
        self.assertEqual(xor_operation(message, key), answer)

    def test_answer_2(self):
        message = bytes.fromhex("68656c6c6f")
        key = bytes.fromhex("6b6579")
        answer = bytes.fromhex("030015070a")
        self.assertEqual(xor_operation(message, key), answer)

    def test_answer_3(self):
        key = bytes.fromhex("a55a")
        message = bytes.fromhex("00010203feff")

        answer = bytes.fromhex("a55ba7595ba5")
        self.assertEqual(xor_operation(message, key), answer)


    def test_empty_message(self):
        self.assertEqual(xor_operation(b"", b"key"), b"")

    def test_key_repeats(self):
        key = b"key"
        message = b"test message"
        encrypted = xor_operation(message, key)
        decrypted = xor_operation(encrypted, key)

        self.assertEqual(decrypted, message)

    def test_long_key(self):
        key = b"helloworld"
        message = b"test"
       

        encrypted = xor_operation(message, key)
        decrypted = xor_operation(encrypted, key)

        self.assertEqual(decrypted, message)

    def test_multibyte(self):
        message = "€¢"
        key = b"key"

        self.assertEqual(
            decrypt(key, encrypt(key, message)),
            message
        )

    def test_non_integer_len(self):
            with self.assertRaises(ValueError):
                int("test")

    
    def test_missing_len(self):
            with self.assertRaises(TypeError):
                int(None)
    
    def test_keygen(self):
        key = keygen(10)

        self.assertEqual(len(key), 10)
        self.assertIsInstance(key, bytes)


    def test_empty_key(self):
        with self.assertRaises(ValueError):
            xor_operation(b"test", b"")


    def test_odd_hex(self):
        with self.assertRaises(ValueError):
            bytes.fromhex("a")



    def test_invalid_hex(self):
        with self.assertRaises(ValueError):
            bytes.fromhex("gz")


    def test_hex_whitespace(self):
        with self.assertRaises(ValueError):
            hex_to_bytes(" helloworld ")


    def test_zero_len(self):
        with self.assertRaises(ValueError):
            length = 0
            if length <= 0:
                raise ValueError()

    def test_negative_len(self):
        with self.assertRaises(ValueError):
            length = -1

            if length <= 0:
                raise ValueError()


    def test_invalid_utf8(self):
        with self.assertRaises(UnicodeDecodeError):
            decrypt(b"\x01", b"\xfe")


if __name__ == "__main__":
    unittest.main()