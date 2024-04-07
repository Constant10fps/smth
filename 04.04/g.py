def makeList(n: int) -> list[dict[str, int]]:
    a: list[dict[str, int]] = list()
    for _ in range(n):
        letters = dict()
        word = input()
        for ch in word:
            letters[ch] = letters.get(ch, 0) + 1
        a.append(letters)
    return a

def countChars(word: dict[str, int], win_ch: str) -> tuple[int, int]:
    good = 0
    other = 0
    for ch in "abcde":
        if ch == win_ch:
            good = word.get(ch, 0)
        else:
            other += word.get(ch, 0)
    return good, other

def countWords(b: list[tuple[int, int]]) -> int:
    count = 0
    sum_good = 0
    sum_other = 0
    for good, other in b:
        sum_good += good
        sum_other += other
        if sum_good <= sum_other:
            break
        count += 1
    return count

def main(n: int) -> int:
    ans = 0
    a = makeList(n)
    
    for win_ch in "abcde":
        b: list[tuple[int, int]] = list()
        for word in a:
            b.append(countChars(word, win_ch))
        b.sort(key=lambda x: x[0] - x[1], reverse=True)
        
        count = countWords(b)
        ans = max(ans, count)
    
    return ans

t = int(input())
for i in range(t):
    n = int(input())
    print(main(n))