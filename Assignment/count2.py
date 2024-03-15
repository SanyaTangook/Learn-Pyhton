def Count2_func(strbin):
    count , countk = 0 , 0
    for i in range(len(strbin)):
        num = int(strbin[i])
        if num == 0:
            countk+=1
        elif num == 1:
            if countk >= count:
                count = countk
                countk = 0
            continue
    return count

n = int(input("input number : "))
strbin = list(str(bin(n))[2::])
print(strbin)
count = Count2_func(strbin)
print(count)