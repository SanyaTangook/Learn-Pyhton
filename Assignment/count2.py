n = int(input("input number : "))
count , countk = 0 , 0

strbin = list(str(bin(n))[2::])

print(strbin)
for i in range(len(strbin)):
    num = int(strbin[i])
    if num == 0:
        countk+=1
    elif num == 1:
        if countk >= count:
            count = countk
            countk = 0
        continue

print(count)