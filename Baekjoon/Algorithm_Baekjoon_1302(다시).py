#딕셔너리 약하다. 쉬운건데 다시해보자.
import sys


def bestseller(n):
    booklist={}
    for _ in range(n):
        book = sys.stdin.readline().strip()
        if book not in booklist:
            booklist[book] = 1
        else:
            booklist[book] += 1

    large_value = max(booklist.values())
    bestsellers=[]

    for book,count in booklist.items():
        if count == large_value:
            bestsellers.append(book)

    return sorted(bestsellers)[0]

n=int(input())

print(bestseller(n))