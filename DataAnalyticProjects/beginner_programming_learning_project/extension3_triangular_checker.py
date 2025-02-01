"""
File: extension3_triangular_checker.py
Name:
Time Spent: 18min 35sec
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


# 因為所有的三角形數都滿足"該數乘2會等於兩個連續正整數相乘"，
# 所以只需要看2倍的使用者輸入值可不可以等於兩個正整數相乘，即可判斷其是否是三角形數
def main():
    """
    After asking user to enter a number, this program will check
    whether that number multiplied by two can be the product of
    two consecutive positive integers.
    """
    print("Welcome to the triangular number checker!")
    while True:
        number = int(input("n: "))
        if number == EXIT:
            break
        check = number * 2                                              # 先做一個2倍使用者輸入值的變數，等等用於判斷
        n = 1                                                           # 正整數從1開始，所以n先設成1
        while True:                                                     # 此回圈是在一直幫我做“是否有連續兩個正整數相乘可以等於兩倍使用者輸入值”的判斷
            if check == n * (n+1):                                      # 若兩倍的使用者輸入的數等於兩個連續正整數相乘，他是三角形數
                print(str(number) + " is a triangular number.")
                break
            elif check > n * (n+1):                                     # 代表還沒有找完“全部的兩續正整數相乘可不可以是2倍的使用者輸入數值”的可能性，應繼續往下一個數找
                n += 1                                                  # 下一個數是n+1
            else:                                                       # 這個區間代表n*(n+1)已經大於2倍使用者輸入值，故接下來的所有連續正整數相乘都不可能等於2倍使用者輸入值，
                print(str(number) + " is not a triangular number.")     # 所以使用者輸入值就不可能是三角形數
                break
    print("Have a good one!")






# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
