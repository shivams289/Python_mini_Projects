def solve(n, s, d, h):
    # n = number of plates
    # d =  destination
    # h = helper
    if n == 1:
        print(f"moving plate {n} from s to d")

    solve(n - 1, s, h, d)
    print("moving n from s to d")
    solve(n - 1, h, d, s)
