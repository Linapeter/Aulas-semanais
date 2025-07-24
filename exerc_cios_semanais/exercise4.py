# Exercicio 2: Sum squares difference

limit = 101

sum_of_squares = (sum(sum_of_squares**2 for sum_of_squares in range(1,limit)))

b = ((sum(i for i in range(1,limit)))**2)

print(b - sum_of_squares)