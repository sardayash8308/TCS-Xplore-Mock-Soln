def removeDuplicate(d:str):
    d = d.lower()
    ans = ""
    for i in d:
        if i not in ans:    ans+=i
    return ans
print(removeDuplicate(input("Enter String : ")))