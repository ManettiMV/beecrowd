"""
Considering the input of non-negative integer values​​, sort these numbers ​​according to the 
following criteria: First the even in ascending order followed by the odd in descending order.

Input
The first line of input contains a positive integer number N (1 < N <= 105). This is the 
number of following input lines. The next N lines contain, each one, a integer non-negative number.

Output
Print all numbers according to the explanation presented above. Each number must be printed
in one line as shown below.
"""
N = int(input())


pares = []
impares = []

for _ in range(N):
    number = int(input())
    if number%2 == 0:
        pares.append(number)
    else:
        impares.append(number)

pares.sort()
impares.sort(reverse=True)

for par in pares:
    print(par)
for impar in impares:
    print(impar)

