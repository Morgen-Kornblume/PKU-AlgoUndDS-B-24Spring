
str1,str2,str3 = "","",""

def calc(h1 : int, h2 : int) -> bool:
    global str1,str2,str3
    #print("%s %s %s" % (str1[h1], str2[h2], str3[h1+h2]))
    if(h1 + h2 == len(str3)):
        return True
    ret = False
    if(h1 < len(str1) and str1[h1] == str3 [h1+h2]):
        ret = ret or calc(h1 + 1, h2)
    if(h2 < len(str2) and str2[h2] == str3 [h1+h2]):
        ret = ret or calc(h1, h2 + 1)
    return ret
n = int(input())

for i in range(n):
    str1, str2, str3 = input().split()
    #print("%s %s %s" % (str1, str2, str3))
    ans = calc(0,0)
    print("Data set ",end="")
    print(i+1,end="")
    print(": ",end="")
    if ans == True:
        print("yes")
    else:
        print("no")
