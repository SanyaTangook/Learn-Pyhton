string = ["flow" ,"flower" ,"flood"]

result = ""
messenger = ""

for i in string:
    if len(messenger) < len(i):
        messenger = i
    elif messenger != i:
        for x in range(len(i)):
            if i[x] in messenger[x]:
                result+=i[x]

print("Longest COmmon Prefix of :" ,string ,": are" ,result)