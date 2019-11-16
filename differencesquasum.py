"""Problem 3

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
For a given number N, find the difference between the sum of the squares of the first N natural numbers and the square of the sum.

Sample Input 
3

Sample Output 
22"""

n=int(input('enter n value:'))
numbers = range(1, n+1)
sum_squares = sum(i**2 for i in numbers)
square_sum = sum(numbers)**2
print('difference:',square_sum - sum_squares)
