"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'                                        # 原始字母序列


def main():
    """
    This program asks user to enter a secret number,
    creates a ciphered sequence based on that number,
    asks user to enter a ciphered string based on that number,
    deciphers the ciphered string, and then print the result.
    """
    secret_number = int(input('Secret number: '))                              # 跟使用者要加密數字
    ciphered_seq = cipher_sequence(ALPHABET, secret_number)                    # 用原字母序列和加密數字來做出加密的字母序列
    ciphered_string = input("What's the ciphered string? ")                    # 跟使用者要加密過的字串
    deciphered_string = decipher(ciphered_string, ciphered_seq, ALPHABET)      # 解密。會用到使用者給的加密字串、加密後的字母序列、原始字母序列
    print('The deciphered string is: ' + deciphered_string)                    # 把解密的內容印出來


def cipher_sequence(alphabet, secret_number):                                  # 此Function在做出加密的字母序列
    """
    : param alphabet: string, the original Alphabet sequence
    : param secret_number: int, the number used to create ciphered sequence
    : return: string, the ciphered alphabet sequence obtained through the
    shift of the end of original alphabet sequence to the front.
    """
    ans = ''                                                                   # 先做出空竹籤
    front = alphabet[len(alphabet)-secret_number:]                             # 字母串長度減Secret_number剛好是要的字母串的第一個字母的index
    end = alphabet[:len(alphabet)-secret_number]                               # 上限不包，所以放剛剛抓出的index作為上限且從頭開始抓即可
    ans = front + end                                                          # 把後面的字串往前丟就得到加密序列了
    return ans


def decipher(ciphered_string, ciphered_seq, alphabet):                         # 查看加密字串在加密字母序中的編號，再去用它們來找出原始字母序列中對應的字
    """
    : param ciphered_string: string, the ciphered string user enters
    : parm ciphered_seq: string, the ciphered sequence based on secret_number
    : param alphabet: string, the original alphabet sequence
    : return: string, the deciphered string obtained through the use of the
    index of the ciphered string on its ciphered sequence.
    """
    ans = ''                                                                   # 先生出空竹籤，等等用來串解密後的字串
    for i in range(len(ciphered_string)):                                      # 查看使用者輸入之加密字串中的每個字是空格、英單、還是其他符號
        if ciphered_string[i] == " ":                                          # 代表加密內容是空格
            ans = ans + " "                                                    # 直接照印空格接上去即可
        elif ciphered_string[i].isupper():                                     # 代表加密的是大寫字母，所以我們可直接去
            index = ciphered_seq.find(ciphered_string[i])                      # 找到使用者輸入的加密文字在加密的字母序列中的index
            ans = ans + alphabet[index]                                        # 並去看該index在正常的字母字串中是啥單字，再塞給新的串
        elif ciphered_string[i].islower():                                     # 代表加密的是小寫字母，但加密的字母序列中沒有小寫
            index = ciphered_seq.find(ciphered_string[i].upper())              # 所以要先把該字母轉大寫再去找加密字母序列中對應的大寫的index
            ans = ans + alphabet[index]                                        # 有了index就可以回去對照原始字母串抓出對應的字並塞給新串
        else:                                                                  # 代表加密內容不是空格或字母
            ans = ans + ciphered_string[i]                                     # 直接把該符號照印上去即可
    return ans                                                                 # 得到解密的結果並丟出Function





















# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
