"""Module with the solution to test."""


def solution(a, x):
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return m

        if a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return -1


if __name__ == "__main__":
    num_list = list(map(int, input().split()))
    x = int(input())
    print(solution(num_list, x))
