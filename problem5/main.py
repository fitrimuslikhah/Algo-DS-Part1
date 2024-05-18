def max_sequence(arr):
    max_current = max_global = arr[0]

    for num in range(1, len(arr)):
        max_current = max(arr[num], max_current + arr[num])
        if max_current > max_global:
            max_global = max_current
    
    return max_global

    
print(max_sequence)

if __name__ == "__main__":
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_sequence([-2, -5, 6, -2, -3, 1, 5, -6]))    # 7
    print(max_sequence([-2, -3, 4, -1, -2, 1, 5, -3]))    # 7
    print(max_sequence([-2, -5, 6, -2, -3, 1, 6, -6]))    # 8
    print(max_sequence([-2, -5, 6, 2, -3, 1, 6, -6]))     # 12