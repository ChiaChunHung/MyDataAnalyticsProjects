"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program will first obtain an answer of the hangman game
    by using random_word function and then ask user to guess the
    answer with limited number of wrong guesses available until
    user win or lose with no available wrong guesses left.
    """
    answer = random_word()                                                  # 取得隨機單字作為謎題的答案
    first_word_look = first_look_of_word(answer)                            # 得到初始的The word looks like ------
    process(first_word_look, answer, N_TURNS)                               # 開始玩：猜字母->判斷對或錯->對給字母/錯減一條命->告知剩幾次可猜


def first_look_of_word(answer):                                             # 創造出一開始的多個dash
    """
    : param answer: string, a answer that will be used to create
    a string filled with dashes whose quantity is based on the
    number of letters of the answer.
    """
    word_look = ''
    for i in range(len(answer)):                                            # 正確答案有幾個字母，
        word_look += '-'                                                    # 一開始就有幾個dash
    return word_look


def process(first_word_look, answer, n_turns):                              # 此Function會讓使用者一直玩此遊戲，直到輸掉或勝出
    """
    : param first_world_look: string, a string showing the letter user
    correctly guessed and dashes that represent the letters user hasn't
    guess correctly
    : param answer: string, the answer of the game created by random_word()
    : param n_turns: int, the number of wrong guesses player left
    """
    while True:                                                             # 離開此回圈後，此Function就終止，因為下面沒有其他code了
        if n_turns != 0:                                                    # 代表還有可以猜的次數，還沒輸
            if first_word_look != answer:                                   # 此區間代表還沒輸，但也還沒贏，故還要繼續猜
                print('The word looks like: ' + first_word_look)            # 告知使用者目前word長相
                print('You have ' + str(n_turns) + ' wrong guesses left')   # 告知還剩幾次可猜
                while True:                                                 # 此回圈一直要求使用者輸入字母，直到字母猜對或猜錯才離開
                    guess = input('Your guess: ')
                    if guess.isalpha():                                     # 判斷是否是字母
                        guess = guess.upper()                               # 判斷是字母後，轉大寫，因是case-insensitive
                        if len(guess) == 1:                                 # 判斷是不是只輸入一個字母
                            if guess in answer:                             # 是字母且只有一個字後，就判斷該字母是不是在答案中
                                ans = ''                                    # 字母是在答案中，在新的空竹籤上串上他。這裏先做空竹籤
                                for i in range(len(answer)):                # 此回圈loop over answer string並一直做判斷
                                    if answer[i] == guess:                  # 若是answer中的某個位置上的字母等於使用者猜對的字母
                                        ans += guess                        # 則新竹籤此刻串上使用者猜中的字母
                                    else:                                   # 若不等於，
                                        ans += first_word_look[i]           # 則新竹籤此刻串上原本first_word_look上的字(之前猜對字或dash)
                                first_word_look = ans                       # 把first_word_look更新
                                print('You are correct!')
                                break                                       # 猜對代表該輪結束，離開此回圈，但外圈下方沒有程式，所以回到外圈開頭
                            else:                                           # 此區間代表猜錯
                                print('There is no ' + guess + ' in the word.')
                                n_turns -= 1                                # 故可猜次數要減1
                                break                                       # 離開此回圈，告知使用者word目前長相＆剩餘可猜次數
                        else:                                               # 此區間代表使用者輸入的是字母，但多輸入一或多個字，所以要求重輸
                            print('Illegal format.')                        # 告知完後，會回到此while loop的開頭，要求使用者輸入
                    else:                                                   # 此區間代表使用者輸入的不是字母，所以要求重輸
                        print('Illegal format.')                            # 告知完後，會回到此while loop的開頭，要求使用者輸入
            else:                                                           # 此區間代表使用者全部的字母都猜出，且次數沒有歸零
                print('You win!!')
                print('The answer is: ' + answer)
                break                                                       # 使用者勝出，故離開最外層while loop，又離開後下方沒有code，故結束
        else:                                                               # 此區間代表使用者把次數用光，輸掉了
            print('You are completely hung :(')
            print('The answer is: ' + answer)
            break                                                           # 離開最外層while loop，又因其下方沒有code，故Function結束


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# 下方是我一開始寫出來的版本。助教改的時候可直接略過，只是想留作紀念XD～
# def main():
#     n = N_TURNS
#     answer = random_word()
#     word = ''
#     for i in range(len(answer)):                                        # 做出起始世界的樣子
#         word = word + '-'
#     while True:
#         if n != 0:
#             if word != answer:
#                 print('The word looks like: ' + word)
#                 print('You have ' + str(n) + ' wrong guesses left.')
#                 while True:
#                     guess = input('Your guess: ')
#                     if guess.isalpha():                                 # 切邊界條件
#                         if len(guess) == 1:                             # 此區間才是可以玩遊戲的區間
#                             guess = guess.upper()
#                             if guess in answer:
#                                 print('You are correct!')
#                                 for i in range(len(answer)):            # 要在這裡切是否前面有找過同樣的字
#                                     if answer[i] == guess:
#                                         guess_index_in_answer = i
#                                         ans = ''
#                                         for j in range(len(word)):
#                                             if j == guess_index_in_answer:
#                                                 ans = ans + guess
#                                             else:
#                                                 ans = ans + word[j]
#                                         word = ans
#                                 break
#                             else:
#                                 print('There is no ' + guess + ' in the word.')
#                                 n = n - 1
#                                 break
#                         else:
#                             print('Illegal format.')
#                     else:
#                         print('Illegal format.')
#             else:
#                 print('You win!!')
#                 print('The answer is: ' + answer)
#                 break
#         else:
#             print('You are completely hung :(')
#             print('The answer is: ' + answer)
#             break



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
