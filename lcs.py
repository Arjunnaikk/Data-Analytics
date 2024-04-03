def print_lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Compute LCS using dynamic programming
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Function to print all LCS
    def print_all_lcs(i, j, lcs, solutions):
        if i == 0 or j == 0:
            lcs_str = ''.join(lcs[::-1])
            if lcs_str not in solutions:
                solutions.add(lcs_str)
                print('LCS:', lcs_str)
            return

        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            print_all_lcs(i - 1, j - 1, lcs, solutions)
            lcs.pop()
        elif dp[i - 1][j] > dp[i][j - 1]:
            print_all_lcs(i - 1, j, lcs, solutions)
        elif dp[i][j - 1] > dp[i - 1][j]:
            print_all_lcs(i, j - 1, lcs, solutions)
        else:
            print_all_lcs(i - 1, j, lcs, solutions)
            print_all_lcs(i, j - 1, lcs, solutions)


    print("LCS Table:")
    for row in dp:
        print(row)

    print("\nDirections:")
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                print("0", end=" ")
            elif X[i - 1] == Y[j - 1]:
                print("↖", end=" ")
            elif dp[i - 1][j] >= dp[i][j - 1]:
                print("↑", end=" ")
            else:
                print("←", end=" ")
        print()

    print("\nAll Possible Solutions:")
    solutions = set()
    print_all_lcs(m, n, [],solutions)

# Take user input for strings X and Y
X = input("Enter string X: ")
Y = input("Enter string Y: ")

print_lcs(X, Y)