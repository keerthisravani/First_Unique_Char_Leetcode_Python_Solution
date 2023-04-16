def firstUniqChar(s):
    map={}
    for i in s:
        if i not in map:
            map[i]=1
        else:
            map[i]+=1
    for i in range(len(s)):
        if map[s[i]]==1:
            return i
    return -1
n="leetcode"
print(firstUniqChar(n))