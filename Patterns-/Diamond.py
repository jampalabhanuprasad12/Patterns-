a = int(input("Enter the number of stars should be in middle: "))
for i in range(1, a + 1): 
    f=(" "*(a-i))   
    b=("* "*i)    
    print(f+b)   
for j in range(a,0,-1):
    d=(" "*(a-j))
    e=("* "*(j))
    print(d+e)