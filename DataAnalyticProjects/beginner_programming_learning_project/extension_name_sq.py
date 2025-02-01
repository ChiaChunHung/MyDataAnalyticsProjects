"""
File: name_sq.py (extension)
Name: 
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main():
    """
    This program will first ask user to enter a name
    and then print the name in a square pattern.
    """
    print('This program prints a name in a square pattern!')
    name = input('Name: ')
    print(name)                                                 # 最上面那一列字
    middle_part(name)                                           # 中間兩欄的字
    reverse(name)                                               # 最底部的字


def middle_part(name):
    """
    This function will print the middle part of
    the square.
    """
    for i in range(len(name)-2):
        print(name[i+1], end='')
        for j in range(len(name)-2):
            print(' ', end='')
        print(name[len(name)-i-2])


def reverse(name):
    """
    This function will reverse the name the user
    enters and print it at the bottom of the square.
    """
    ans = ''
    for i in range(len(name)):
        ans = name[i] + ans
    print(ans)





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
