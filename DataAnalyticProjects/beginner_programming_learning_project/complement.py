"""
File: complement.py
Name:
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    This program help users find the Complementary fragments
    of the nitrogenous bases that they enter.
    """
    print(build_complement('ATC'))          # build_complement()可以被Print，所以他會有Return，因是在print他的return
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    : param dna: string
    : return: string, return complementary fragments of nitrogenous bases
    that the users enter.
    """
    if dna == '':                           # 先切邊際條件：分成“輸入空字串”和“非輸入空字串”
        return 'DNA strand is missing.'
    else:                                   # 進入此區間代表使用者輸入特定含氮鹼基序列，下方開始幫她找互補鹼基序列
        ans = ''                            # 先做空竹籤
        for i in range(len(dna)):           # 每圈都幫我判斷是ATCG中的哪個值。下方的if/elif/else每一圈都只會擇一執行
            if dna[i] == 'A':               # 若字母是A
                ans += 'T'                  # 那就幫我換成互補鹼基T
            elif dna[i] == 'T':             # 若字母是T
                ans += 'A'                  # 那就幫我換成互補鹼基A
            elif dna[i] == 'C':             # 若字母是C
                ans += 'G'                  # 那就幫我換成互補鹼基G
            else:                           # 剩餘條件是，字母為G
                ans += 'C'                  # 那就幫我換成互補鹼基C
        return ans                          # 因為main中有在print此Function，所以該Function要設置return.




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
