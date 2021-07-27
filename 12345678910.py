w=int(input("NO. OF ROWS IN YOUR PATTERN:"))
current=1
for i in range(0,w+1):
    for j in range(0,i+1):
        print(current,end="")
        current += 1
    print("\r")