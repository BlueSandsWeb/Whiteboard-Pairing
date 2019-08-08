def contiguous_sum(arr):
    largest_sum = 0
    largest_set = []
    current_sum = 0
    current_list = []
    for i in range(len(arr)):
        current_list.append(arr[i])
        # track current sum in an array
        current_sum += arr[i]
        if current_sum > largest_sum:
            largest_list = current_list
            largest_sum = current_sum
        if current_sum <= 0:
            current_list = []
            current_sum = 0
    print(largest_list)
    return largest_sum


                

print(contiguous_sum([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))