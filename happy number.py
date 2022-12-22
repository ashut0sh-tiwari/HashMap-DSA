"""Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not."""

n = 19

def isHappy(n):
        chain = set()  #initialising a hash set
        while n !=1: #loopind until n not equals to 1
            n = sum(int(i)**2 for i in str(n)) #converting n into str and then iterating elements and adding their squares using type conversion again by making them integers
            if n in chain: #check if n already is in set then return false as it will stuck in endless loop
                return False
            else: #check if n already is in set and if not then adding that value in set
                chain.add(n)
        else: #if n =1 return true
            return True

sol = isHappy(n)
print(sol)