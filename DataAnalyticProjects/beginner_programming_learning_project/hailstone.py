"""
File: hailstone.py
Name: Tony
Time spent: 33 min 54 sec. (not include note)
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program tells users how many steps it will take
    for the number they enter to reach number 1 under the law of
    the Hailstone sequence.
    """
    print("This program computes Hailstone sequences.")
    n = int(input("Enter a number: "))
    if n == 1:                                                          # 先判斷進入的資料是不是來亂的
        print("It took 0 steps to reach 1.")
    else:                                                               # 進入資料不是來亂的，開始執行hail stone sequence.
        steps = 0                                                       # 目的是為了等等計算到底跑了幾次回圈。跑幾次就代表做了多少steps。
        while n != 1:                                                   # 開關是當n=1時，就離開迴圈
            if n % 2 == 1:                                              # 判斷奇數偶數。奇數進yes區；偶數進else區
                n_1 = n * 3 + 1                                         # 這邊一定先把n*3+1assign給n_1
                print(str(n)+" is odd"+", so I make 3n+1: "+str(n_1))   # 如此，這裏印出時，才能print出處理前的數字和處理後的數字
                n = n_1                                                 # 把n reassign n_1，才不會變無限迴圈（我們是把處理後的結果丟回去開關再繼續判斷）
                steps += 1                                              # 每跑一圈加一次
            else:
                n_1 = int(n/2)                                          # 老師的範例沒有浮點數，所以用int()。一樣要把處理後的結果先assign給n_1。
                print(str(n) + " is even" + ", so I take half: " + str(n_1))
                n = n_1                                                 # 把n reassign n_1，才不會變無限迴圈（我們是把處理後的結果丟回去開關再繼續判斷）
                steps += 1                                              # 每跑一圈加一次
        print("It took "+str(steps)+" steps to reach 1.")               # 當算到n=1時，就跳出回圈並把steps數量印出來。




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
