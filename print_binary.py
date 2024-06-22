def print_binary(n, prefix=""):
    if n == 1:
        if prefix != "":
            print(prefix, 0)
        else:
            print(0)
        if prefix != "":
            print(prefix, 1)
        else:
            print(1)
    else:
        if prefix != "":
            print(prefix)
            print_binary(prefix, n - 1, 0)
        else:
            print_binary(n - 1, 0)

        if prefix != "":
            print(prefix)
            print_binary(prefix, n - 1, 1)
        else:
            print_binary(n - 1, 1)


ans = []

print_binary(3, ans)
