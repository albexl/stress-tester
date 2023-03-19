"""Module with the correct solution. Just for illustrative purposes."""


def solution(a, x):
    l = 0
    r = len(a) - 1
    pos = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] >= x:
            pos = m
            r = m - 1
        else:
            l = m + 1

    return pos


if __name__ == "__main__":
    num_list = list(map(int, input().split()))
    x = int(input())
    print(solution(num_list, x))
