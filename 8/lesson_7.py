


def pair_sum_sequense(n: int) -> int:  # O(N)
    sum = 0
    while sum < n:
        sum += 1
        print(sum)
    return sum


def pair_sum(a, b): # O(1)
    return a + b



letters = ['a', 'b', 'c', 'd', 'e', ]
numbers = [1, 2, 3, 4, 5]

def sum_o(): # O(N**2)
    for n in letters:
        print(n)
    for n in numbers:
        print(n)

    for n in letters:
        for n in numbers:
            print(f"{n} {n}")


def mul_o():
    for n in letters:
        for b in numbers:
            print(f"{n} {b}")

# sum_o()
mul_o()

a = [1, 3, 5, 2, 1, 4, 5]