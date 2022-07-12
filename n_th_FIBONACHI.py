a1, a2, n = map(int,input("Enter an integers a1, a2 and n, separated by single spaces, with condictions 0 < a1, a2, 2 <= n <= 10: ").split())
i = 3
while i <= n:
    an = a1 + a2
    a1 = a2
    a2 = an
    #print(an)
    i += 1
#print("n-th element of the equence is: ", a2) 
print(a2)
