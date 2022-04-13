if __name__ == "__main__":
    a = list(map(int, input().split()))

    d = dict()
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    print(len(d.keys()))

    for key, value in d.items():
        print(key, ":", value)
