# Rotate-Array-by-One-in-python
arr = list(map(int, input("Enter elements: ").split()))
arr = [arr[-1]] + arr[:-1]
print("After rotation:", arr)
