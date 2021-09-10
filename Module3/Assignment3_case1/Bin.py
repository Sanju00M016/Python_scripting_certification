concentrate = [trying for trying in input("Enter the String of Binary Number:").split(",")]
bored = []
for x in concentrate:
    y = int(x, 2)
    if y%5==0:
        bored.append(x)
print(",".join(bored))

# ilist = list(map(str, input("Enter the strings: ").split(',')))
#
# ans = []
# for i in ilist:
#     p = int(i, 2)
#     if p % 5 == 0:
#         ans.append(i)
#print(ans)