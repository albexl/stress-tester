import random


def no_brainer(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


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


def generate_input():
    n = random.randint(1, 10)
    a = [random.randint(1, 10) for _ in range(n)]
    a.sort()
    x = a[random.randint(0, n - 1)]
    return a, x


def debug():
    test_cases = 10000
    for _ in range(test_cases):
        a, x = generate_input()
        no_brainer_output = no_brainer(a, x)
        solution_output = solution(a, x)
        if no_brainer_output != solution_output:
            print("Test Case:")
            print(a, x)
            print("Solution Output:", solution_output)
            print("No-Brainer Output:", no_brainer_output)
            exit()
    print("All test cases passed succesfully")


if __name__ == "__main__":
    debug()
