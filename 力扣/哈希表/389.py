def fun(str1,str2):
    dict= {}
    for i in str1:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1

    for i in str2:
            dict[i] -= 1

    for k in dict.keys():
         if dict[k]!=0:
              return k
str2 = "abcde"
str1 = "eabfcd"
print(fun(str1,str2))

'''
list = [0]*26
str1 = 'abcdee'
str2 = 'cbaeedf'
for i in str1:
    list[ord(i)-ord('a')] += 1
for i in str2:
    list[ord(i)-ord('a')] -= 1

for i in range(26):
    if list[i] != 0:
        print(chr(i+ord('a')))
'''