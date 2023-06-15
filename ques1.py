def levenshtein_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    # Create a 2D matrix to store the distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Calculate the Levenshtein distance
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,  # deletion
                    dp[i][j - 1] + 1,  # insertion
                    dp[i - 1][j - 1] + 1  # substitution
                )

    return dp[m][n]

# Test the function
string_a = "ot6z3nmlcghn"
string_b = "fbn957yrg87v"
distance = levenshtein_distance(string_a, string_b)
print(f"The Levenshtein distance between '{string_a}' and '{string_b}' is {distance}.")
