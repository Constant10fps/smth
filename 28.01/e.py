n = int(input())
prices = list(map(int, input().split()))
idx = [i for i in range(n) if prices[i] == max(prices)]
print(idx[0]+1, max([i for i in prices if i != max(prices)]))
'''
print(idx, end = " ")
prices.remove(max(prices))
print(max(prices))
'''