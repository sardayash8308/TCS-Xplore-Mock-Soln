s = input("Enter String : ")
alp_count = 0
space = 0
for i in s:
    if i.isalpha(): alp_count+=1
    elif i.isspace():   space+=1
print(f"No of spaces : {space} and characters : {alp_count}")
