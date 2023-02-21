def fact_rec(n):
    if n == 1:
        return n
    else:
        return n * fact_rec(n - 1)


number = int(input("Enter number:"))

if number == 0:
    print('not possible')
elif number == 1:
    result = fact_rec(number)
    print(result)
# else:
#     result = fact_rec(number)
#     print(result)

# normal
else:
    fact = 1
    for i in range(1, number + 1):
        fact = fact*i
    print(fact)

