import re

def problem1():
    cipher_text = "ROYQWH KQXXJYQ: N LQGNQAQ HDJH FO. VW NX J KQKLQO VZ J XQMOQH MONKQ VOYJWNSJHNVW MJGGQF U.D.J.W.H.V.K., IDVXQ YVJG NX HVHJG IVOGF FVKNWJHNVW. HDQNO UGJW NX HV JMBRNOQ J XRUQOIQJUVW JWF HV DVGF HDQ IVOGF OJWXVK. N JK JZOJNF HDJH IQ FV WVH DJAQ KRMD HNKQ LQZVOQ HDQT XRMMQQF.\nN DJAQ OQMQWHGT NWHQOMQUHQF JW QWMOTUHQF KQXXJYQ (JHHJMDKQWH MNUDQO2.HCH) HDJH IJX XQWH LT FO. VW HV VWQ VZ DNX MVWXUNOJHVOX, HDQ NWZJKVRX KO. LGVIZNQGF. N KJWJYQF HV FNXMVAQO HDJH HDQ KQXXJYQ IJX QWMOTUHQF RXNWY HDQ PJMEJG MNUDQO (XQQ XVROMQ MVFQ), LRH N IJX WVH JLGQ FNXMVAQO HDQ XQMOQH EQT, JWF HDQ MNUDQO XQQKX HV LQ RWLOQJEJLGQ. N JK JZOJNF HDJH FQMOTUHNWY HDNX KQXXJYQ NX HDQ VWGT IJT HV XHVU FO. VW'X VOYJWNSJHNVW.\nUGQJXQ XQWF OQNWZVOMQKQWHX NKKQFNJHQGT! N HONQF HV JMH MJRHNVRXGT, LRH N DJAQ J ZQQGNWY HDJH FO. VW'X DQWMDKQW JOQ VWHV KQ. N FVW'H EWVI DVI GVWY N DJAQ LQZVOQ HDQT FNXMVAQO KT OQJG NFQWHNHT JWF KT XQMOQH DNFNWY UGJ"

    def ComputeFrequency(cipher_text):
      freq = {}
      for char in set(cipher_text):
        freq[char] = cipher_text.count(char)
      return  freq

    freqList = ComputeFrequency(cipher_text)
    print("Frequency Table for ciphertext below:")
    for char in sorted(freqList):
      if char.isalpha():
        print(f"{char}:{freqList[char]}")
        # print(f"{char}: {round(freqList[char]/len(cipher_text), 3)}") 

    Substitution = {'A': 'v', 'B':'q', 'C':'x', 'D':'h', 'E':'k', 'F':'d', 'G':'l',
       'H':'t','I':'w', 'J':'a', 'K':'m', 'L':'b', 'M':'c','N': 'i',
       'O':'r', 'P':'j','Q':'e', 'R':'u', 'S': 'z', 'T':'y', 'U':'p',
       'V':'o', 'W':'n','X': 's','Y':'g', 'Z':'f'}
  
    decrypted_text = ""
    for char in cipher_text:
      if char.isalpha():
          char = char.upper()
          decrypted_text += Substitution[char]
      else:
          decrypted_text += char 
    print("\nDecrypted Text:\n")
    # END SOLUTION
    print(decrypted_text)


def JACKAL_Decrypt(firstKeyByte, secondKeyByte, cipherText):
# returns a plaintext bytearray 
    x = (firstKeyByte + 31)
    y = (secondKeyByte * 3)
    p = []
    for z in range(len(cipherText)):
        x = (x + 29) & 0xFF
        y = (y * 19) & 0xFF
        p.append(cipherText[z] ^ x ^ y)
    return bytearray(p)

def isEnglishText(byte):
    punctuations = ".,'-:{}"
    try:
        for char in byte.decode('utf-8'):
            if not (char.isalnum() or char.isspace() or char in punctuations):
                return False
    except UnicodeDecodeError as e:
        return False
    return True

def Problem2():
    with open("cipher2.txt", "rb") as file:
        cipherText = file.read()
    # BEGIN SOLUTION
    
    found = False
    for i in range(128):
        for j in range(128):
            plainText = JACKAL_Decrypt(i, j, cipherText)
            if isEnglishText(plainText): 
                found = True
                break

        if found:
            break
  
    # END SOLUTION
    print(plainText.decode('utf-8'))


def problem3():
    with open("cipher3.txt", "rb") as file:
        cipher_text = file.read()
    # BEGIN SOLUTION
    key = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    plain_text = bytearray(len(cipher_text))

    curr = 0
    for i in range(len(plain_text)):
        if curr == 11:
            curr = 0
        plain_text[i] = cipher_text[i] ^ key[curr]
        curr += 1
    
    # END SOLUTION
    print(plain_text.decode('utf-8'))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n\nProblem 1 \n\n")
    problem1()
    print("\n\nProblem 2 \n\n")
    Problem2()
    print("\n\nProblem 3 \n\n")
    problem3()
