n = 5  # You can change this to set the number of rows for the diamond pattern

if n % 2 == 0:
    print("Please use an odd number of rows.")
else:
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))
