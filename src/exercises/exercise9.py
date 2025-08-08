## 2420 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
## What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

number = 0
stop = 0
lista = [1,10]
while stop!= 1:
    for i in lista:
        if number%i == 0:
            stop = 1
        else:
            number += 1
