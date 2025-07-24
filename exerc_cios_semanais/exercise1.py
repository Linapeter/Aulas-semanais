# Week 1

# Exercise 1
# Execute a code that returns the sum of multiples of 3 and 5 up to the number n
# Ex: with n=10, the multiples are [3,5,6,9] and the sum is 23
print("Choose a number:")
n = int(input())
multiples = list()
for i in range (1,n):
    if i%3==0 or i%5==0:
        multiples.append(i)

print("The sum of the multiples is", sum(multiples))

# Correção
# Aqui, não crio uma lista que consome muita memória
total = 0
for i in range(1, 1000):
    if i%3 == 0 or i%5 == 0:
        total += i
print("The sum of the multiples is", total)
