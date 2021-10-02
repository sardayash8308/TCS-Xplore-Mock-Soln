def func(s:str):
    k = 'aeiou'
    vowelCount = 0;consonantsCount = 0
    for i in s:
        if i.isalpha():
            if i in k:  vowelCount+=1
            else:   consonantsCount+=1
    return f"Vowels Count - {vowelCount}\nConsonants count - {consonantsCount}"

print(func(input("Enter String : ")))



