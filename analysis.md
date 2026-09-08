# Analysis
## Zoe Eigenbrod
## 9/7/2026

## Correctness

In xor_vigenere.py, an encrypted message can be decrypted and output the same starting message. The function xor_operation takes in values for a message and a key. An XOR operation is conducted on each bit for the message using the corresponding bit from the key, with the key repeating in cases where the message is shorter than the key. Xor_operation is reversible and used for encryption and decryption in this program. To prove $\mathsf{Dec}_k(\mathsf{Enc}_k(m))=m$ for every $m\in\mathbb{B}^*$ and every $k\in\mathbb{B}^+$, we need to look at how an XOR operation works. Encryption uses an XOR operation against the message and the key, and decryption uses an XOR operation against the result of the encryption XOR. This means that the key (k) performs the operation on itself, leaving just the message (m) after decryption[1]. This can be represented as 
$$
(m_i\oplus k_i)\oplus k_i=m_i
$$

## Known Plaintext

An attacker can derive the key byte if they know the message bytes and the corresponding ciphertext bytes. The key is the ciphertext and the message combined by the XOR operation. This can be represented as $$
k_i = c_i \oplus m_i
$$ 
If the key is shorter than the message, it will repeat itself. Using pattern recognition from the repetition, you can reveal the key. If the key is the same length or longer than the message, the attacker will not be able to use this tactic[2]. 

## Key reuse

When two messages of equal length are encrypted using the same repeating key, you can derive how the two messages relate to each other, and the key is canceled out of the messages. This can be represented as $$ c_i \oplus c'_i = (m_i \oplus k_i) \oplus (m'_i \oplus k_i) = m_i \oplus m'_i$$.
The result is the two messages combined together with the XOR operation. The actual decrypted messages in plaintext are not revealed with this alone. Even so, an attacker can use the information from performing the XOR operation on the two ciphertexts to reveal information about the decrypted messages[3]. 

## One time pad

For a one time pad, the two parties involved must both know the key. The key must completely uniformly random. Additionally, the one time pad needs to have a length that is at least as long as the original message. Finally, the key can not be used more than one time. Repeating key XOR does not fulfill these requirements in the situations where the length of the key is less than the length of the original message. Additionally, it does not meet these requirements when the key is used more than once[4]. 

## Security Limits

Given two cases:
1. A short key that repeats within a message.
2. A uniformly random key at least as long as the message and is never reused.

The confidentiality obtained is different for each case. For the case of a short repeating key, it may not be as secure because an attacker can use the repeating pattern to determine the key. For the second case regarding a one-time use uniformly random key as long as the message, it is more confidential because you can’t determine the key from any sort of repetition[4].

# Sources
## 1. Carnegie Mellon University 
[Cryptography](https://s22.cs251.com/Text/19_Cryptography/media_upload/Cryptography.pdf)

## 2. NVISO Labs
[XOR Known-Plaintext Attacks](https://blog.nviso.eu/2023/10/12/xor-known-plaintext-attacks/)

## 3. Crypto 101
[Exclusive or](https://crypto101.multun.net/exclusive-or.html)

## 4. University of Toronto
[The One-Time Pad and Perfect Secrecy](https://www.cs.toronto.edu/~david/course-notes/csc110-111/08-cryptography/02-one-time-pad.html)
