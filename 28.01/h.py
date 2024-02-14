n = int(input())
out = ""
fib = [1, 2]
for i in range(n):
    if i+1 == fib[-1] + fib[-2]:
        fib.append(i+1)
    if i+1 in fib:
        out += "O"
    else:
        out += "o"
print(out)