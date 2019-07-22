"""
Use a stack to convert integer values to binary.

ex. 242

242/2 = 121 -> 242 % 2 = 0
121//2 = 60 -> 121 % 2 = 1
60/2 = 30 -> 60 % 2 = 0
30/2 = 15 -> 30 %2 = 0
15/2 = 7 -> 15 %2 = 1
7/2 = 3 -> 1
3/2 = 1 -> 1
1/ 2 = 0 -> 1

"""

from stack import Stack

def div_by_2(num):
    s = Stack()

    while num > 0:
        remainder = num % 2
        s.push(remainder)
        num = num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

print div_by_2(242)
