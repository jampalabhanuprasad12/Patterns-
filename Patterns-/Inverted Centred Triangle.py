a=int(input("Enter the number of rows that you want to print:"))
for i in range(a,0,-1):
    b=("  "*(a-i))
    c=("* "*(2*i-1))
    print(b+c)