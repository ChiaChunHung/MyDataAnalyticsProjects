"""
File: extension2_number_checker.py
Name: Tony
Time Spent: 41 min
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""

# 當使用者輸入EXIT時，即可離開程式
EXIT = -100


# 找出使用者輸入值的真因數的加總，接者只要比大小即可
def main():
    """
    After asking user to enter a number, this program will first find
    out all the proper factors of that number, and then it will calculate
    the sum of all those factors to determine whether the result is equal,
    higher, or lower than the number the user enters.
    """
    print("Welcome to the number Checker!")
    while True:                                                 # 此回圈會一直要求讀者輸入值以及判斷其真因數的和和自己的大小關係
        number = int(input("n: "))                              # 要求讀者輸入一筆值
        if number == EXIT:                                      # 若該值是EXIT(邊界條件)，那就離開回圈
            break
        count_from = 1                                          # 此變數目的是用來找出所有真因數。因為因數從1開始找，故起始值設1
        summary = 0                                             # 此變數用來裝真因數的加總。
        while True:
            if number == count_from:                            # 不用計算自己是不是自己的因數，因為目的是要找真因數
                break                                           # 故回圈走到計算自己是不是自己的真因數時，就跳開
            else:                                               # 此區間代表還在找自己的真因數
                if number % count_from == 0:                    # 當發現真因數時
                    summary = summary + count_from              # 就把該真因數加近真因數加總的結果中
                    count_from = count_from + 1                 # 先不用count_from +=1的寫法，因會一直忘記這是加1並Reassign給自己
                else:
                    count_from = count_from + 1                 # 不是真因數，就+1進入下個回圈去看下個數字是否是自己的真因數
        if summary == number:                                   # 得到真因數加總後，開始判斷該總和和使用者輸入值的大小關係
            print(str(number)+" is a perfect number.")
        elif summary > number:
            print(str(number)+" is an abundant number.")
        else:
            print(str(number) + " is a deficient number.")
    print("Have a good one!")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
