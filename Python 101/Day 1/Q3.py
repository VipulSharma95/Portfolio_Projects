"""
Question 3 - Put the Q2 logic in a function, add name == '_main_' and make it work
Author - Vipul Sharma
Date - 17/03/2025
Comments - Loop printing function which takes n as an argument uses it to print 100 numbers in main
"""
def num_print(n):
    for i in range(1, n + 1):
        print(i)

if __name__ == '__main__':
    num_print(100)