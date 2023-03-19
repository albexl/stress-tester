"""Module with the naive solution."""


def naive(a, x):
    return next((i for i in range(len(a)) if a[i] == x), -1)


if __name__ == "__main__":
    num_list = list(map(int, input().split()))
    x = int(input())
    print(naive(num_list, x))
