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
    sender = Sender()
    sender.encrypt(plaintext)
    sender.sign() # sign original plaintext

    # modifying plaintext after signing
    pos1 = 0 
    pos2 = 2  
    modified_plaintext = plaintext[:pos1] + bytes([plaintext[pos2]]) + plaintext[pos1+1:pos2] + bytes([plaintext[pos1]]) + plaintext[pos2+1:]

    # encrypt the modified plaintext
    modified_cipher = rsa.encrypt(modified_plaintext, sender.public_key)

    # Receiver Side
    receiver = Receiver()
    receiver.decrypt(modified_cipher, sender.public_key, sender.private_key) # decrypt modified ciphertext
    receiver.verify(modified_plaintext, sender.signature, sender.public_key) # verify by comparing sign of original with modified plaintext 

