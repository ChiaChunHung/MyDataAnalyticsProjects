"""
File: extension4_narcissistic_checker.py
Name:
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    After asking user to enter a number, this program will begin to identify
    whether the number is a narcissistic number, by counting the number of the digit of it,
    calculating the sum of its own digits each raised to the power of the number of digits,
    and comparing the sum with the number itself.
    """
    print("Welcome to the narcissistic number checker!")
    while True:
        number = int(input("n: "))
        if number == EXIT:                                      # 判斷使用者是不是一開始就要離開
            break
        if number < 10:                                         # 先切出此區間給“當使用者只輸入個位數字時“使用
            print(str(number) + " is a narcissistic number.")   # 個位數必然是narcissistic number
        else:                                                   # 此區間則是切給十位數含以上的數字
            # 先找出此數字共有幾位數
            num_for_figure = number                             # 把使用者輸入的數字複製到不同的箱子，這樣等等做其他運算時，才可以繼續把使用者的值叫出來用
            figure = 2                                          # 因為已知是10含以上的數，所以位數可以先設至少有2位
            while True:                                         # 此回圈一直幫我做除以10的動作。可以想成：每除10一次，就是小數點由右往左移一次
                if num_for_figure // 10 >= 10:                  # 若除以10，商還剩下大於等於10就代表至少有三位數
                    figure += 1                                 # 此時位數就要加1
                    num_for_figure = num_for_figure // 10       # 因為下一個回圈必須是除過的值在繼繻除下去，所以必須Reassign
                else:                                           # 走到這代表：位數加一位數，就是該數的位數了
                    break
            # 找出位數是幾位後，再找出各位數字的次方後的總和
            sum_of_power = 0                                    # 因為總和一開始得先有數字才能加總，所以先把總和先預設為0
            power = figure - 1                                  # 這裏的power目的是為了等等可以用10的power變數去逼出每位數字的確切數字是啥。power減一是因為若位數是4位，10的3次方就是4位數。
            num_for_digit = number                              # 為了要讓等等還能取用使用者輸入值，所以先把該值也賦予給另外一個等等要做計算的箱子
            while True:                                                                         # 此回圈可以逼出各個位數的數字，在把他們次方後進行加總
                sum_of_power = sum_of_power + ((num_for_digit // (10**power))**figure)          # 計算各位數字次方後的總和
                num_for_digit = num_for_digit - ((num_for_digit // (10**power)) * 10**power)    # 把使用者輸入值計算完一圈後的結果Reassign，才能繼續找下一位數的值
                power -= 1                                                                      # 每做一個回圈，10的次方項就少一
                if power == 0:                                                                  # 此時代表使用者輸入的值已經被除到個位數了，所以就把最後的個位數做次方後，加入總和得到結果
                    sum_of_power = sum_of_power + num_for_digit**figure
                    break
            # 接者判斷該總和是否等於自己
            if sum_of_power == number:
                print(str(number) + " is a narcissistic number.")
            else:
                print(str(number) + " is not a narcissistic number.")
    print("Have a good one!")








# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()