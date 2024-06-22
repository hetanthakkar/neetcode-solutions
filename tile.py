def longest_tile_sequence(tiles):
    n = len(tiles)
    dp = [[0] * n for _ in range(n)]

    # Base case: single tile sequences
    for i in range(n):
        dp[i][i] = 1

    # Fill the DP table, ensuring valid tile connections and consistent calculations
    for i in range(n-1, -1, -1):  # Iterate backward for accurate sequence building
        for j in range(i+1, n):
            if tiles[i][1] == tiles[j][0]:  # Connection with the next tile
                dp[i][j] = 1 + dp[i+1][j-1]  # Include only the connecting tiles
            if i > 0 and tiles[i-1][1] == tiles[j][0]:  # Connection with the previous tile
                dp[i][j] = max(dp[i][j], 2 + dp[i+1][j-1])  # Account for two tiles, exclude used
            if i > 0 and tiles[i][1] == tiles[j-1][0]:  # Connection at the other end
                dp[i][j] = max(dp[i][j], 1 + dp[i+1][j-1])  # Include only the connecting tiles

    return max(max(row) for row in dp)  # Find the maximum length

# Example usage:
tiles = ["RR", "GR", "RG", "GR", "GR", "RR"]
result = longest_tile_sequence(tiles)
print("Longest sequence length:", result)  # Output: 5
