"""
File: string_score.py
Name:
------------------------------
This program calculates a score for a given string based on 
the types of characters it contains. It assigns points as follows: 
digits are worth 1 point, uppercase letters are worth 2 points, 
and lowercase letters are worth 3 points. The score() function 
goes through each character in the string, adds up the points 
according to its type, and then prints out the total score.
"""


def main():
    """
    This program calculates a score for a given string, whose
    score is based on the types of characters it contains.
    """
    score('1aB4rC')
    score('aaaaA3')


def score(string):                     # 此Function幫我用for loop判斷每個每個字是大寫、小寫、還是數字並幫我按照他們的分數做加總
    """
    : param string: string, the string that is used to calculate a score.
    """
    summary = 0                        # 先設一個變數箱子拿來裝加總的結果
    for i in range(len(string)):       # 字母有幾個就需要做幾圈，每一圈都只會擇下方其中一個條件做執行
        if string[i].isdigit():        # 若字串string的第i號門是數字，
            summary += 1               # 總分+1
        elif string[i].isupper():      # 若字串string的第i號門是大寫，
            summary += 2               # 總分+2
        else:                          # 剩餘條件為“字串string的第i號門是小寫”，
            summary += 3               # 此時總分+3
    print(summary)                     # 因為main中該Function左邊沒接，此Function就不用return；但又要讓他印出結果，所以就在Function中要求他把結果print出來




if __name__ == '__main__':
    main()