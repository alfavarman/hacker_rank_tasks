import math

# n number of all pages in the book. len(book)
n = 5

# randomly opened page
# p = (1, 2, 3, 233, 261, 262, 522, 523)
i = (range(1, n+1))


# if n in half of the book we need open book from front to make less pages turn
for p in i:
    if p == 1 or p == n:
        pages_to_turn = 0
    elif p < (n/2):
        pages_to_turn = p // 2
    elif p in range(n//2, n//2+2):
        pages_to_turn = n//4
    else:
        pages_to_turn = math.ceil((n-p) / 2)
    print(f'for page number {p} you need to turn {pages_to_turn}')


