import random


def generate_input():
    n = random.randint(1, 10)
    a = [random.randint(1, 10) for _ in range(n)]
    a.sort()
    x = a[random.randint(0, n - 1)]
    return a, x


if __name__ == "__main__":
    a, x = generate_input()
    print(len(a))
    print(" ".join([str(elem) for elem in a]))
    print(x)
