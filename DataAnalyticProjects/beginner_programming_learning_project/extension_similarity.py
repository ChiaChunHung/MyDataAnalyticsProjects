"""
File: similarity.py (extension)
Name:
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program will ask user to give a DNA sequence to search
    and a DNA sequence the user wants to match and find the segment
    of the DNA sequence to search that match best to the DNA sequence
    the user want to match.
    """
    given_dna_seq = input('Pleas give me a DNA sequence to search: ')
    match_seq = input('What DNA sequence would you like to match? ')
    find_the_best_match(given_dna_seq, match_seq)                                       # 會找出和使用者輸入片段相似度最高的原DNA片段


# 注意：算取到哪時，要小心自己的開頭位置加上自己的長度，會剛好略過自己
def find_the_best_match(given_dna_seq, match_seq):
    """
    : param given_dna_seq: string, the DNA sequence to search
    : param match_seq: string, the DNA sequence the user wants to match
    """
    given_dna_seq = given_dna_seq.upper()
    match_seq = match_seq.upper()
    # 下一行開始處理第一筆進入的資料
    count = 0                                                                           # 先設一個裝配對成功次數的空箱子
    compared_seg = given_dna_seq[:len(match_seq)]                                       # 抓出第一組DNA片段來和使用者輸入片段做配對
    for i in range(len(match_seq)):                                                     # loop over 使用者輸入＆原始的DNA片段
        if match_seq[i] == compared_seg[i]:                                             # 看同位置的字母在使用者輸入片段和原始片段中是否匹配
            count += 1                                                                  # 匹配則成功次數+1
    maximum = count                                                                     # 第一組DNA片段的配對成功次數先上王座
    best_match_seq = compared_seg                                                       # 第一組DNA片段先上相似度最高片段的王座
    # 此處開始處理第二筆和之後的資料
    first_index_of_last_seg = (len(given_dna_seq) - 1) - (len(match_seq) - 1)           # 抓出左至右最大可取到哪個index才不會超出原始DNA片段
    for i in range(1, first_index_of_last_seg+1):                                       # 從第二組DNA片段一直到最後一組DNA片段
        compared_seg = given_dna_seq[i:i+(len(match_seq))]                              # 抓出每一組原片段的樣子
        count = 0                                                                       # 準備空箱子裝此片段的配對成功次數
        for j in range(len(match_seq)):                                                 # loop over 使用者輸入＆原始的DNA片段
            if match_seq[j] == compared_seg[j]:                                         # 看同位置的字母在使用者輸入片段和原始片段中是否匹配
                count += 1                                                              # 匹配則成功次數+1
        if count >= maximum:                                                            # 比較新一組片段的配對成功次數和王座上那組的成功次數
            maximum = count                                                             # 若新一組片段的匹配成功次數勝出則成功次數王座換人坐
            best_match_seq = compared_seg                                               # 同時相似度最高片段的王座也換人坐
    print('The best match is ' + best_match_seq)                                        # 最後就會得出匹配成功次數最高的那組，印出來即可

















# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
