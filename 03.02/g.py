n, x = map(int, input().split())
cards = sum(list(map(int, input().split())))
print(abs(-cards)//x if cards%x == 0 else abs(-cards)//x + 1)