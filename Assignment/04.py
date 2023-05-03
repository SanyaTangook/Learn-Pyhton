x = input()
arr = []
for i in range(len(x)):
    arr.append(x[i])
    if (arr[0] == '-'):
        arr[0] = '-' + x[1]
    arr[i] = int(arr[i])
arr.reverse()
if (arr[-1] < 0):
    arr[0] *= -1
    del arr[-1]
    arr[-1] = abs(arr[-1])
elif (arr[-1] == 0):
    arr.remove(0)

print(int(''.join(map(str, arr))))
