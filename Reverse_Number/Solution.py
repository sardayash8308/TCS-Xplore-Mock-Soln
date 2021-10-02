def soln(a):
    l = 0
    if a==0:
        return l
    else:
        if a<0: 
            a = a * -1
            l = soln(a) * -1
        else:
            while(a!=0):
                l = 10*l + a%10
                a//=10
        return l

a = int(input("Enter Your Number : "))
print(soln(a))

