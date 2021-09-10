Number = []
for num in range(900,2500):
   num_1 = str(num)
   if(int(num_1[0])%2==0) and (int(num_1[1])%2==0) and (int(num_1[2])%2==0) and (int(num_1[3])%2==0):
        Number.append(num_1)
print(",".join(Number))

#tried to understand, but couldn't understand this Program.