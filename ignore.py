import timeit

# Initialize with -1
stmt1 = """
value = -1
value == -1
"""

# Initialize with None
stmt2 = """
value = None
value is None
"""

time_taken1 = timeit.timeit(stmt1, number=1000000)
time_taken2 = timeit.timeit(stmt2, number=1000000)

print(f"Time taken with -1: {time_taken1:.6f} seconds")
print(f"Time taken with None: {time_taken2:.6f} seconds")
