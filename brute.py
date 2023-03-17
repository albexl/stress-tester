def no_brainer(a, x):
    return next((i for i in range(len(a)) if a[i] == x), -1)


if __name__ == "__main__":
    n = int(input())
    num_list = list(map(int, input().split()))
    x = int(input())
    print(no_brainer(num_list, x))
