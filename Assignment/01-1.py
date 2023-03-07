import time
a = input("Enter a number: ")
aList = list(a)
output = ""

i = len(aList) - 1
while i >= 0:
    output+=aList[i]
    i -= 1

if (a.endswith("0")):
    output = output[1:]
elif (a.__contains__("-")):
    output = "-" + output.replace("-", "")
s=time.time()
print("Reverse number is : "+output)