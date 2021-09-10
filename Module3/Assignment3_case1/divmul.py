divmul = []
for i in range(2000,3200):
    if (i%7==0) and not (i%5 == 0):
        divmul.append(str(i))
print(','.join(divmul))

