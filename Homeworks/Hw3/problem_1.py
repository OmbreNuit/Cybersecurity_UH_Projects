# This is the template for Problem 1 only.
# For problems 2 and 3, keep the class definitions
# the same and rewrite the main program
import rsa
key_size = 2048

class Sender:
    # BEGIN SOLUTION
    def __init__(self):
        self.message =  None
        self.public_key, self.private_key = rsa.newkeys(key_size)
        self.hash = None
        self.signature = None
        self.cipher = None

    def encrypt(self, message):
        self.message = message
        self.cipher = rsa.encrypt(message, self.public_key)
        # print("Encrypted message: ", self.cipher)

    def sign(self):
        self.hash = rsa.compute_hash(self.message, 'SHA-256')
        self.signature = rsa.sign_hash(self.hash, self.private_key, 'SHA-256')

    # END SOLUTION

class Receiver:
    # BEGIN SOLUTION
    def __init__(self):
        self.plainText = None
        self.public_key = None
        self.private_key = None
        self.signature = None
        self.cipherText = None

    def decrypt(self, cipher, publicKey, privateKey):
        self.cipherText = cipher
        self.public_key = publicKey
        self.private_key = privateKey
        self.plainText = rsa.decrypt(self.cipherText, self.private_key)
        print("Decrypted message: ", self.plainText.decode('utf-8'))

    def verify(self, message, signature, sender_public_key):
        self.signature = signature
        try:
            print('Verification: ', rsa.verify(message, self.signature, sender_public_key))
        except rsa.VerificationError:
            print('Verification Failed')
    # END SOLUTION

if __name__ == "__main__":
    with open('message1.txt', 'rb') as file:
        plaintext = file.read()
    
    # Sender Side
    # BEGIN SOLUTION
    sender = Sender()
    sender.encrypt(plaintext)
    sender.sign()
    # END SOLUTION

    # Receiver Side
    # BEGIN SOLUTION
    receiver = Receiver()
    receiver.decrypt(sender.cipher, sender.public_key, sender.private_key)
    receiver.verify(sender.message, sender.signature, sender.public_key)    
    # END SOLUTION