l = list(map(int,input().split()))

def isPrime(a:int)->bool:
    if a<=1:    return False
    else:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:  return False
        else:   return True

arr = []

for i in l:
    if(isPrime(i)):
        arr.append(i)
arr.sort()
print(arr[-2]+len(arr))
