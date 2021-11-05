n = int(input("Enter an integer: "))


def odd_sum(n):
    k = 0
    for i in range(1, n+1, 2):
        k = k + i
    return k


def even_avg(n):
    k = 0
    for i in range(0, n + 1, 2):
        k = k + i
    return k/n


print("The sum of the odd numbers until the given integer is: ", odd_sum(n))
print("The average of the sum of even numbers till the given number is: ", even_avg(n))
