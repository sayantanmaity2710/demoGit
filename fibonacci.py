nterm = int(input("Enter number:"))
n1, n2 = 0, 1
count = 0
if nterm <= 0:
    print('not possible')
elif nterm == 1:
    print('squence:', nterm)
    print(n1)
else:
    while count < nterm:
        print(n1)
        nth = n1 + n2
        n1 = nth
        n2 = n1
        count += 1